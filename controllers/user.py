#importando o documento Tree
# -*- coding: utf-8 -*-
from models import mongoOP
import pymongo

dbuser = mongoOP.OpMongoDB('forestbd', 'users')

dbuser.collection.create_index([("email", pymongo.ASCENDING)], unique=True)

def createUser(dados):
    return dbuser.save(dados)

def uploadUser(id, dados):
    return dbuser.upload(id, dados)

def patchUser(id, dados):
    return dbuser.patch(id,dados)

def deleteUser(id):
    return dbuser.remove(id)

def listUser():
    return dbuser.list()

def getUser(id):
    return dbuser.findById(id)
