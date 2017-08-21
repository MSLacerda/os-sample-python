#importando o documento Tree
# -*- coding: utf-8 -*-
from models import mongoModel
from bson.json_util import dumps

# Metodo para salvar nova arvore
def createTree(data):
    # Documento
    tree = mongoModel.Tree(nome_pop=data.nome_pop, );
    response = {
        "Error": False,
        "Messange": 0
    }
    # Tenta Salvar o documento com os dados recebidos
    try:
        tree.save();
        response = {
            "Error": False,
            "Message": "Tree added with success!"
        }
    except e as Exception:
        response = {
            "Error": True,
            "Message": "Error: " + e
        }
    
    return dumbs(response);
    
def deleteTree():
    # TODO
    
def listTrees():
    trees = mongoModel.Tree();
    return dumps(trees.objects());

    
def getTree():
    pass
    # TODO
