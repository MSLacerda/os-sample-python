#importando o documento Tree
# -*- coding: utf-8 -*-
from models import mongoOP
from bson.json_util import dumps

def createTree(data):
    mg = mongoOP.OpMongoDB('forestbd', 'trees')
    return dumps(mg.save(data))
    
def deleteTree():
    pass
    # TODO
    
def listTrees():
    mg = mongoOP.OpMongoDB('forestbd','trees')
    return dumps(mg.list())
    
def getTree():
    pass
    # TODO
