# -*- coding: utf-8 -*-

# Este modulo carrega todas as funções do flas
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from flask import Flask
from werkzeug.routing import BaseConverter, ValidationError
from itsdangerous import base64_encode, base64_decode
from bson.objectid import ObjectId
from bson.errors import InvalidId

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
import json

# Flass app
application = Flask(__name__)
application.url_map.converters['objectid'] = ObjectIDConverter
CORS(application)
# Rota index para teste

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
                    ACTIVITIES
----------------------------------------------------
"""

@application.route("/activities", methods=['POST','GET', 'DELETE'])
def ctrlAct():
    if (request.method == 'POST'):
        pass  # TODO
    elif (request.method == 'GET'):
        return "This router works :)"
    elif (request.method == 'DELETE'):
        pass #TODO 






    
