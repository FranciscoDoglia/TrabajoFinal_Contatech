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

@app.route('/consulta/<id>', methods=['GET']) #se refiere al ID del cliente
def consulta(id):
    cliente_list = []
    cliente_id = db.session.query(Cliente).filter_by(id = id)
    for cliente in cliente_id:
        cliente_dict = {"nombre": cliente.nombre, "documento":cliente.documento, "id":cliente.id}
        cliente_list.append(cliente_dict)
    return json.dumps(cliente_list)

@app.route('/consulta/<id>', methods=['DELETE']) #se refiere al ID del cliente
def delete_cliente(id):
    cliente_list = []
    cliente_id = db.session.query(Cliente).filter_by(id=id)
    for cliente in cliente_id:
        cliente_deleted = {"nombre": cliente.nombre, "documento":cliente.documento, "id":cliente.id}
        cliente_list.append(cliente_deleted)
    cliente_id = db.session.query(Cliente).filter_by(id=id).delete()
    db.session.commit()
    return f'Ha eliminado al siguiente cliente: {cliente_list}'

@app.route('/consulta/<id>', methods=['PUT']) #se refiere al ID del cliente
def modify(id):
    request_json = request.json
    nombre = request_json['nombre']
    documento = request_json['documento']
    cliente_id = db.session.query(Cliente).filter_by(id = id).update({"nombre" : nombre, "documento" : documento})
    db.session.commit()
    return f'El cliente id:{id} se ha modificado.\nSu nombre actual es: {nombre}, y su documento es: {documento}'

@app.route('/consulta/<id>/portal_factura/add_factura', methods=['POST']) #se refiere al ID del cliente
def datos_factura(id):
    request_json = request.json
    c = db.session.query(Cliente).filter_by(id = id).first()
    numero = request_json['numero']
    new_factura = Factura(numero)
    new_factura.cliente_id = c.id
    db.session.add(new_factura)
    db.session.commit()
    return f'''Buenos días, usted ha creado la siguiente factura: número:{new_factura.numero}, 
    y fue emitida para el cliente ID:{new_factura.cliente_id}, nombre: {new_factura.parent.nombre}, 
    documento: {new_factura.parent.documento}'''    #PARA PROBAR USAR API https://inspector.swagger.io/builder

@app.route('/portal_factura/consulta', methods=['GET']) 
def consulta_factura_all():
    factura_list = []
    factura_id = db.session.query(Factura).all()
    for factura in factura_id:
        factura_dict = {"ID":factura.id, "numero": factura.numero, "pertenece al Cliente: ": factura.parent.nombre,
                        "documento": factura.parent.documento}
        factura_list.append(factura_dict)
    return json.dumps(factura_list)


@app.route('/portal_factura/consulta/<id>', methods=['GET']) #se refiere al ID de la factura
def consulta_factura(id):
    factura_list = []
    factura_id = db.session.query(Factura).filter_by(id = id)
    for factura in factura_id:
        factura_dict = {"numero": factura.numero, "pertenece al Cliente: ":factura.parent.nombre, "documento": factura.parent.documento}
        factura_list.append(factura_dict)
    return json.dumps(factura_list)

@app.route('/portal_factura/consulta/<id>', methods=['DELETE']) #se refiere al ID de la factura
def delete_factura(id=id):
    facturas_list = []
    factura_id = db.session.query(Factura).filter_by(id=id)
    for factura in factura_id:
        factura_deleted = {"numero": factura.numero, "del Cliente ": factura.parent.nombre, "documento": factura.parent.documento}
        facturas_list.append(factura_deleted)
    factura_id = db.session.query(Factura).filter_by(id=id).delete()
    db.session.commit()
    return f'Ha eliminado la siguiente factura: {facturas_list}'
#Faltaría hacer que los numeros de factura no pueden estar repetidos por cliente, es decir, maría ID tanto,

@app.route('/portal_factura/consulta/<id>', methods=['PUT']) #se refiere al ID de la factura
def modify_factura(id):
    request_json = request.json
    numero = request_json['numero']
    factura_id = db.session.query(Factura).filter_by(id = id).update({"numero" : numero})
    db.session.commit()
    return f'La factura ID:{id} se ha modificado.\nSu numero actual es: {numero}'



if __name__ == '__main__':
    app.run(debug=True, port=8080)
    db.Base.metadata.create_all(db.engine)
    run()
