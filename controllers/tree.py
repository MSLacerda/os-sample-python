#importando o documento Tree
# -*- coding: utf-8 -*-
from bson.json_util import dumps
from models import mongoOP

bdtree = mongoOP.OpMongoDB('forestbd','trees')

def createTree( dados):
    return bdtree.save(dados)

def uploadTree(id,dados):
    return bdtree.upload(id, dados)

def deleteTree(id):
    return bdtree.remove(id)
    
def listTrees():
    return bdtree.list()
    
def getTree(id):
    return bdtree.findById(id)

def addLoc(id, dados):
    return bdtree.patch(id, dados)