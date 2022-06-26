from flask import Flask, request, json, jsonify
import db
from model import Cliente

app = Flask(__name__)


def run():
    pass

@app.route('/add_client', methods=['POST'])
def datos_cte():
    request_json = request.json
    nombre = request_json['nombre']
    documento = request_json['documento']
    new_client = Cliente(nombre, documento)
    db.session.add(new_client)
    db.session.commit()
    return f'{new_client.nombre}Hello {new_client.documento}, {new_client.id}'
    #PARA PROBAR USAR API https://inspector.swagger.io/builder

@app.route('/consulta')
def consulta():
    myCliente = db.session.query(Cliente).all() #Cliente.query.all()
    return jsonify(myCliente)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
    run()
