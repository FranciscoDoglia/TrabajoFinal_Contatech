from flask import Flask, request, json, jsonify
import db
from model import Cliente

app = Flask(__name__)


def run():
    pass

@app.route('/')
def home():
    return "Bienvenido al Facturador Online"

@app.route('/add_client', methods=['POST'])
def datos_cte():
    request_json = request.json
    nombre = request_json['nombre']
    documento = request_json['documento']
    new_client = Cliente(nombre, documento)
    db.session.add(new_client)
    db.session.commit()
    return f'Buenos días, usted ha creado el siguiente usuario: {new_client.nombre}, documento:{new_client.documento}, ID: {new_client.id}'
    #PARA PROBAR USAR API https://inspector.swagger.io/builder

@app.route('/consulta')
def consulta():
    cliente_dict = {}
    myCliente = db.session.query(Cliente).all() #Cliente.query.all()
    for cliente in myCliente:

        clientes_d0 = {"nombre": cliente.nombre}
        clientes_d1 = {"documento": cliente.documento}
        cliente_dict[cliente.id] = [clientes_d0, clientes_d1]

    return json.dumps(cliente_dict)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
    db.Base.metadata.create_all(db.engine)
    run()
