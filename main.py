from flask import Flask
from flask_restx import Api

import config

app = Flask(__name__) 

api = Api(app,
            version='1.0',
            title="Gerenciador de Tarefas",
            description="Aplicação para gerenciar tarefas - Devaria 2021",
            doc="/docs")

if __name__ == '__main__':
    app.run(host=config.API_HOST, port=config.API_PORT, debug=config.DEBUG)