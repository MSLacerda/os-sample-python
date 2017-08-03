# -*- coding: utf-8 -*-

# Este modulo carrega todas as funções do flas
from flask import Flask, request

# Importando controller de teste
from controllers import tree

# Flass app
application = Flask(__name__)

# Rota index para teste


@application.route("/tree", methods=['POST','GET', 'DELETE'])
# Função da rota index
def ctrlTree():
    if (request.method == 'POST'):
        pass  # TODO
    elif (request.method == 'GET'):
        return "This router works :)"
    elif (request.method == 'DELETE'):
        pass  # TODO

@application.route("/user", methods=['POST','GET', 'DELETE'])
def ctrlUser():
    if (request.method == 'POST'):
        pass  # TODO
    elif (request.method == 'GET'):
        return "This router works :)"
    elif (request.method == 'DELETE'):
        pass #TODO 
        
@application.route("/activities", methods=['POST','GET', 'DELETE'])
def ctrlAct():
    if (request.method == 'POST'):
        pass  # TODO
    elif (request.method == 'GET'):
        return "This router works :)"
    elif (request.method == 'DELETE'):
        pass #TODO 






    
