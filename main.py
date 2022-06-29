from flask import Flask, request, json, jsonify
import db
from model import Cliente, Factura

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

@app.route('/consulta', methods=['GET'])
def consulta_all():
    cliente_list = []
    myCliente = db.session.query(Cliente).all() #Cliente.query.all()
    for cliente in myCliente:
        cliente_dict = {"nombre": cliente.nombre, "documento":cliente.documento, "id":cliente.id}
        cliente_list.append(cliente_dict)
    return json.dumps(cliente_list)

@app.route('/consulta/<id>', methods=['GET'])
def consulta(id):
    cliente_list = []
    cliente_id = db.session.query(Cliente).filter_by(id = id)
    for cliente in cliente_id:
        cliente_dict = {"nombre": cliente.nombre, "documento":cliente.documento, "id":cliente.id}
        cliente_list.append(cliente_dict)
    return json.dumps(cliente_list)

@app.route('/consulta/<id>', methods=['DELETE'])
def delete_client(id):
    cliente_list = []
    cliente_id = db.session.query(Cliente).filter_by(id=id)
    for cliente in cliente_id:
        cliente_deleted = {"nombre": cliente.nombre, "documento":cliente.documento, "id":cliente.id}
        cliente_list.append(cliente_deleted)
    cliente_id = db.session.query(Cliente).filter_by(id=id).delete()
    db.session.commit()
    return f'Ha eliminado al siguiente cliente: {cliente_list}'

@app.route('/consulta/<id>', methods=['PUT'])
def modify(id):
    request_json = request.json
    nombre = request_json['nombre']
    documento = request_json['documento']
    cliente_id = db.session.query(Cliente).filter_by(id = id).update({"nombre" : nombre, "documento" : documento})
    db.session.commit()
    return f'El cliente id:{id} se ha modificado.\nSu nombre actual es: {nombre}, y su documento es: {documento}'

@app.route('/add_factura', methods=['POST'])
def datos_factura():
    request_json = request.json
    # client_id = request_json['client_id']
    numero = request_json['numero']
    new_factura = Factura(numero)
    db.session.add(new_factura)
    db.session.commit()
    return f'Buenos días, usted ha creado la siguiente factura: número:{new_factura.numero}'    #PARA PROBAR USAR API https://inspector.swagger.io/builder


if __name__ == '__main__':
    app.run(debug=True, port=8080)
    db.Base.metadata.create_all(db.engine)
    run()
