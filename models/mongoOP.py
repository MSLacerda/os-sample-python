# -*- coding: utf-8 -*-

from pymongo import MongoClient
import json


class OpMongoDB():
    client = MongoClient(
        'mongodb://mslacerda:chaos456@ds015915.mlab.com:15915/forestbd')

    # Construtor db = banco de dados, collection
    def __init__(self, db, collection):
        self.db = self.client.get_database(db)
        self.collection = self.db.get_collection(collection)

    def save(self, dados):
        response = {}
        if not dados._id:
            try:
                 inserted_id = self.collection.insert_one(dados).inserted_id
                 response = {
                     "error": False,
                     inserted_id: inserted_id
                 }
        else:
            self.collection.update(dados)

    def remove(self, id):
        # TODO
        pass

    def list(self):
        # TODO
        pass

    def findById(self, id):
        # TODO
        pass
