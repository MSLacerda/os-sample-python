# Codificação alaterada para utf8
# -*- coding: utf-8 -*-

# Este modulo carrega todas as funções do flas
from flask import Flask
# Importando controller de teste
from controllers import nothing



# Flass app

application = Flask(__name__)

# Rota index para teste
@application.route("/index")
# Função da rota index
def index(): 
    return nothing.hello()


