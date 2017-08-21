# -*- coding: utf-8 -*-
# Importa mongocliente para realizar a conexão com bd do mongo criado
from pymongo import MongoClient
from flask import jsonify
import json
import sys
from bson.json_util import dumps
from bson.objectid import ObjectId

# Classe definida para disponibilizar operações com o mongodb
# define e cria conexão e inserção, remoção, atualização e re-
# cuperação de dados
class OpMongoDB():
    # client = MongoClient('mongodb://mslacerda:chaos456@ds015915.mlab.com:15915/forestbd')
    client = MongoClient('localhost', 27017)

    # Construtor db = banco de dados, collection
    def __init__(self, db, collection):
        self.db = self.client.get_database(db)
        self.collection = self.db.get_collection(collection)

    # Metodo para atualizar ou inserir novos dados
    def save(self, dados):
        
        # Criando variável que armazena a resposta
        response = {}
        # ----------------------------------------
        # Caso exista um id apenas faz o update
        # se não, adiciona um novo
        # ----------------------------------------
        try:
            a= dados['_id']
        except:
            a = None

        if not a:
            # Faz um try catch para garantir inserção dos dados
            try:

                inserted_id = self.collection.insert_one(dados).inserted_id
                response = {
                    "Error": False,
                    "Menssage": "Objeto adicionado com sucesso!",
                    "_id": (str(inserted_id))
                }
            except:
                response = {
                    "error": True,
                    "Menssage": "Error no processamento do serviço!"
                }

            #--------------------------
            # Resposta do servidor
            #--------------------------
            return response
            #-------------------------- 

        else:
            # Caso não exista id é feixo uma atualização com base
            # no id recebido e mais uma vez com segurança que os dados 
            # sejam atualizados
            try:
                print ("tem id")
                inserted = self.collection.update(dados)
                response = {
                    "Error": False,
                    "Menssage": "Arquivo atualizado com sucesso"
                }
            except:
                response = {
                    "error": True,
                    "Menssage": "Error ao processar servicço"
                }

            #--------------------------
            # Resposta do servidor
            #--------------------------
            return response
            #-------------------------- 





    def remove(self, id):
        try:
            res = self.collection.delete_one({"_id": ObjectId(id)})
            # print()
            response = {
                "Error": False,
                "QuatDelete": res.deleted_count,
            }
        except:
            response = {
                "Error": True,
                "Data": "Não foi possivel remover"
            }
        return response





    def list(self):
        response = {}
        try:
            data = self.collection.find()
            data = [x for x in data]
            for x in data:
                x['_id'] = str(x['_id'])

            if (data):
                # print (data)
                response = {
                    "Error": False,
                    "Data": data
                }
            else:
                response = {
                    "Error": True,
                    "Menssage": "Erro ao acessar serviço"
                }
        except Exception as e:
            print(e)
            response = {
                "Error": True,
                "Menssage": "Error no serviço "
            }
        
        return response







    def findById(self, id):
        res = self.collection.find_one({"_id": ObjectId(id)})
        res["_id"] = str(res['_id'])

        return res

