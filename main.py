from flask import Flask, request, json, jsonify
import requests

import db
# from cliente_prueba import Cliente
import model
from model import Cliente

app = Flask(__name__)


def run():
    pass

@app.route('/add_client', methods=['GET', 'POST'])
def datos_cte():
    # nombre = request.args['nombre']
    # documento = request.args['documento']
    request_json = request.json
    # print(request_json['nombre'],request_json['documento'])
    new_client = Cliente(request_json['id'], request_json['nombre'])
    db.session.add(new_client)
    db.session.commit()
    return f'{new_client.id}Hello {new_client.nombre}'
    #PARA PROBAR USAR API https://inspector.swagger.io/builder

@app.route('/consulta')
def consulta():
    myCliente = Cliente.query.all()
    return jsonify(myCliente)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
    db.Base.metadata.create_all(db.engine)
    run()

