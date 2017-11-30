# -*- coding: utf-8 -*-

# Este modulo carrega todas as funções do flas
from flask import jsonify, flash, send_file
from flask_cors import CORS
from werkzeug.routing import BaseConverter, ValidationError
from itsdangerous import base64_encode, base64_decode
from bson.objectid import ObjectId
from bson.errors import InvalidId
import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename


class ObjectIDConverter(BaseConverter):
    def to_python(self, value):
        try:
            return ObjectId(base64_decode(value))
        except (InvalidId, ValueError, TypeError):
            raise ValidationError()
    def to_url(self, value):
        return base64_encode(value.binary)


# Importando controller de teste
from controllers import tree
from controllers import user


UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


# Flass app
application = Flask(__name__,  static_folder='uploads', static_url_path='')
application.url_map.converters['objectid'] = ObjectIDConverter
CORS(application)
application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


"""
----------------------------------------------------
                    TREE
----------------------------------------------------
"""
@application.route("/tree", methods=['POST','GET'])
# Função da rota index
def ctrlTree():
    if (request.method == 'POST'):
        res = tree.createTree(request.json)
        return jsonify(res)

    elif (request.method == 'GET'):
        res = tree.listTrees()
        return jsonify(res)


@application.route('/tree/<idtree>',  methods=['GET', 'DELETE', 'PUT', 'PATCH'])
def getIdTree(idtree):

    if (request.method == "GET"):
        res = tree.getTree(idtree)
        return jsonify(res)

    elif (request.method == 'DELETE'):
        print(idtree)
        res = tree.deleteTree(idtree)
        return jsonify(res)

    elif (request.method == 'PUT'):
        res = tree.uploadTree(idtree,request.json)
        return jsonify(res)

    elif (request.method == 'PATCH'):

        res = tree.addLoc(idtree, request.json)
        return jsonify(res)


"""
----------------------------------------------------
                    USER
----------------------------------------------------
"""


@application.route("/user", methods=['POST','GET'])
# Função da rota index
def ctrlUser():
    if (request.method == 'POST'):
        res = user.createUser(request.json)
        return jsonify(res)

    elif (request.method == 'GET'):
        res = user.listUser()
        return jsonify(res)


@application.route('/user/<iduser>',  methods=['GET', 'DELETE', 'PUT', 'PATCH'])
def getIdUser(iduser):

    if (request.method == "GET"):
        res = user.getUser(iduser)
        return jsonify(res)

    elif (request.method == 'DELETE'):
        print(iduser)
        res = user.deleteUser(iduser)
        return jsonify(res)

    elif (request.method == 'PUT'):
        res = user.uploadUser(iduser,request.json)
        return jsonify(res)

    elif (request.method == 'PATCH'):
        res = user.patchUser(iduser,request.json)
        return jsonify(res)



"""
----------------------------------------------------
                    UPLOADS
----------------------------------------------------
"""

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@application.route('/uploads' , methods=['POST','GET'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)


            file.save(os.path.join(application.config['UPLOAD_FOLDER'], filename))
            res = {
                "completo" : os.path.join(application.config['UPLOAD_FOLDER'], filename),
                "file_name" : filename
                 }
            return jsonify(res)

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''



@application.route('/get_file/<name>' )
def get_file(name):
    try:
        return send_file('../uploads/'+ name,
                         attachment_filename=name)
    except Exception as e:
        return str(e)



    
