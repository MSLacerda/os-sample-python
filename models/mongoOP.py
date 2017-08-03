# -*- coding: utf-8 -*-
# Importa mongocliente para realizar a conexão com bd do mongo criado
from pymongo import MongoClient
import json


# Classe definida para disponibilizar operações com o mongodb
# define e cria conexão e inserção, remoção, atualização e re-
# cuperação de dados
class OpMongoDB():
    client = MongoClient('mongodb://mslacerda:chaos456@ds015915.mlab.com:15915/forestbd')

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
        if not dados._id:
            # Faz um try catch para garantir inserção dos dados
            try:
                inserted_id = self.collection.insert_one(dados).inserted_id
                response = {
                    "Error": False,
                    "Menssage": "Objeto adicionado com sucesso!"
                    "id": inserted_id
                }
            except:
                response = {
                    "error": True,
                    "Menssage": "Error no processamento do serviço!"
                }

            #--------------------------
            # Resposta do servidor
            #--------------------------
            return json.dumps(response)
            #-------------------------- 

        else:
            # Caso não exista id é feixo uma atualização com base
            # no id recebido e mais uma vez com segurança que os dados 
            # sejam atualizados
            try:
                inserted = self.collection.update(dados)
                response = {
                    "Error": False,
                    "Menssage": "Arquivo atualizado com sucesso"
                }
            except:
                response = {
                    "error": True,
                    "Menssage:" "Error ao processar servicço"
                }

            #--------------------------
            # Resposta do servidor
            #--------------------------
            return json.dumps(response)
            #-------------------------- 



    def remove(self, id):
        # TODO
        pass

    def list(self):
        # TODO
        pass

    def findById(self, id):
        # TODO
        pass
