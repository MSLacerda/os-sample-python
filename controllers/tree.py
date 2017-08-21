#importando o documento Tree
# -*- coding: utf-8 -*-
from models import mongoModel
from bson.json_util import dumps

bdtree = mongoOP.OpMongoDB('forestbd','trees')

def createTree( dados):

    return bdtree.save(dados)
    
def deleteTree(id):
    return bdtree.remove(id)
    
def listTrees():

    return bdtree.list()
    
def getTree(id):
    return bdtree.findById(id)
