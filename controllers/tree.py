#importando o documento Tree
# -*- coding: utf-8 -*-
from models import mongoOP


def createTree():
    pass
    # TODO
    
def deleteTree():
    pass
    # TODO
    
def listTrees():
    mg = mongoOP.OpMongoDB('forestbd','trees')
    return mg.list()
    
def getTree():
    pass
    # TODO
