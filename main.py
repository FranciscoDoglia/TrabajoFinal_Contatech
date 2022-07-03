from flask import Flask, request, json, jsonify
import db
from model import Cliente, Factura

app = Flask(__name__)


def run():
    pass

@app.route('/')
def home():
    return "Bienvenido al Facturador Online"


@app.route('/add_cliente', methods=['POST'])
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
def delete_cliente(id):
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

@app.route('/consulta/<id>/portal_factura/add_factura', methods=['POST'])
def datos_factura(id):
    request_json = request.json
    c = db.session.query(Cliente).filter_by(id = id).first()
    numero = request_json['numero']
    ng = request_json['neto_gravado']
    iva = request_json['iva']
    new_factura = Factura(numero, ng, iva)
    new_factura.cliente_id = c.id
    db.session.add(new_factura)
    db.session.commit()
    return f'''Buenos días, usted ha creado la siguiente factura: número:{new_factura.numero}, 
    y fue emitida para el cliente ID:{new_factura.cliente_id}, nombre: {new_factura.parent.nombre}, 
    documento: {new_factura.parent.documento}.
     El monto neto gravado de la factura es: {ng}, el IVA correspondiente: {new_factura.iva} y el total
    del comprobante: {new_factura.total}'''    #PARA PROBAR USAR API https://inspector.swagger.io/builder

@app.route('/portal_factura/consulta', methods=['GET'])
def consulta_factura_all():
    factura_list = []
    factura_id = db.session.query(Factura).all()
    for factura in factura_id:
        factura_dict = {"ID":factura.id, "numero": factura.numero, "Cliente: ": factura.parent.nombre,
                        "documento": factura.parent.documento, "total":factura.total}
        factura_list.append(factura_dict)
    return json.dumps(factura_list)


@app.route('/portal_factura/consulta/<id>', methods=['GET'])
def consulta_factura(id):
    factura_list = []
    factura_id = db.session.query(Factura).filter_by(id = id)
    for factura in factura_id:
        factura_dict = {"numero": factura.numero, "Cliente: ":factura.parent.nombre, "documento": factura.parent.documento, "total":factura.total}
        factura_list.append(factura_dict)
    return json.dumps(factura_list)

@app.route('/portal_factura/consulta/<id>', methods=['DELETE'])
def delete_factura(id=id):
    facturas_list = []
    factura_id = db.session.query(Factura).filter_by(id=id)
    for factura in factura_id:
        factura_deleted = {"numero": factura.numero, "Cliente ": factura.parent.nombre, "documento": factura.parent.documento, "total":factura.total}
        facturas_list.append(factura_deleted)
    factura_id = db.session.query(Factura).filter_by(id=id).delete()
    db.session.commit()
    return f'Ha eliminado la siguiente factura: {facturas_list}'
#Faltaría hacer que los numeros de factura no pueden estar repetidos por cliente, es decir, maría ID tanto,

@app.route('/portal_factura/consulta/<id>', methods=['PUT'])
def modify_factura(id):
    request_json = request.json
    numero = request_json['numero']
    ng = request_json['neto_gravado']
    iva = request_json['iva']
    factura_id = db.session.query(Factura).filter_by(id = id).update({"numero" : numero, "neto_gravado": ng, "alic_iva": iva})
    db.session.commit()
    return f'''La factura ID:{id} se ha modificado.\nSu numero actual es: {numero}. El total de la factura es {ng * (1+(iva/100))},
    el monto neto gravado es: {ng} y el IVA es {ng * (iva/100)}'''



if __name__ == '__main__':
    app.run(debug=True, port=8080)
    db.Base.metadata.create_all(db.engine)
    run()
 
