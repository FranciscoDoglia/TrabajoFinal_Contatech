# TrabajoFinal_Contatech
Error cuando corro el endpoint '/consulta', me dice que no existe atributo query en mis db

Traceback (most recent call last):
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\flask\app.py", line 2095, in __call__
    return self.wsgi_app(environ, start_response)
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\flask\app.py", line 2080, in wsgi_app
    response = self.handle_exception(e)
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\flask\app.py", line 2077, in wsgi_app
    response = self.full_dispatch_request()
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\flask\app.py", line 1525, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\flask\app.py", line 1523, in full_dispatch_request
    rv = self.dispatch_request()
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\flask\app.py", line 1509, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**req.view_args)
  File "C:\Users\frand.LAPTOP-P3HHCD9I\Desktop\Fran\Curso Python\Proyecto fin\main.py", line 29, in consulta
    myCliente = Cliente.query.all()
AttributeError: type object 'Cliente' has no attribute 'query'
127.0.0.1 - - [21/Jun/2022 07:45:58] "GET /consulta?__debugger__=yes&cmd=resource&f=debugger.js HTTP/1.1" 304 -
127.0.0.1 - - [21/Jun/2022 07:45:58] "GET /consulta?__debugger__=yes&cmd=resource&f=style.css HTTP/1.1" 304 -
127.0.0.1 - - [21/Jun/2022 07:45:58] "GET /consulta?__debugger__=yes&cmd=resource&f=console.png HTTP/1.1" 304 -

Otro error:
Cuando quiero hacer que Cliente(db.Base) tenga 3 columnas (id, nombre, documento), e ingresar solamente nombre y documento y que id sea primary key, me da el siguiente error
sqlalchemy.exc.ProgrammingError: (psycopg2.errors.UndefinedColumn) column "documento" of relation "clientes" does not exist
LINE 1: INSERT INTO clientes (nombre, documento) VALUES ('marcos', 1...
                                      ^

[SQL: INSERT INTO clientes (nombre, documento) VALUES (%(nombre)s, %(documento)s) RETURNING clientes.id]
[parameters: {'nombre': 'marcos', 'documento': 1234}]
(Background on this error at: https://sqlalche.me/e/14/f405)
