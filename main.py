from flask import Flask, request, json
# from model import Cliente

app = Flask(__name__)


@app.route('/add_client', methods=['GET', 'POST'])
def datos_cte():
    # nombre = request.args['nombre']
    # documento = request.args['documento']
    request_json = request.json
    # print(request_json)
    return f'Hello {request_json["nombre"]}, ID {request_json["documento"]}'
    y = json.dumps(request_json["nombre"])

    #PARA PROBAR USAR API https://inspector.swagger.io/builder

if __name__ == '__main__':
    app.run(debug=True, port=8080)

class Cliente: #Esta clase es prueba para ver si logro obtener la variable desde request.json
    def __init__(self,nombre: str, documento: str):
        self.nombre = nombre
        self.documento= documento
clientex = Cliente(datos_cte(request_json["nombre"]), datos_cte(request_json["documento"]))
print(clientex)
