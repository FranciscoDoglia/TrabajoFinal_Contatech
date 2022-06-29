
127.0.0.1 - - [29/Jun/2022 18:32:56] "POST /add_client HTTP/1.1" 500 -
Traceback (most recent call last):
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\engine\base.py", line 1819, in _execute_context
    self.dialect.do_execute(
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\engine\default.py", line 732, in do_execute
    cursor.execute(statement, parameters)
psycopg2.errors.UndefinedTable: relation "clientes" does not exist
LINE 1: INSERT INTO clientes (nombre, documento) VALUES ('Marcos', '...
                    ^


The above exception was the direct cause of the following exception:

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
  File "C:\Users\frand.LAPTOP-P3HHCD9I\Desktop\Fran\Curso Python\Proyecto fin\main.py", line 23, in datos_cte
    db.session.commit()
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\orm\session.py", line 1451, in commit
    self._transaction.commit(_to_root=self.future)
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\orm\session.py", line 829, in commit
    self._prepare_impl()
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\orm\session.py", line 808, in _prepare_impl
    self.session.flush()
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\orm\session.py", line 3383, in flush
    self._flush(objects)
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\orm\session.py", line 3522, in _flush
    with util.safe_reraise():
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\util\langhelpers.py", line 70, in __exit__
    compat.raise_(
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\util\compat.py", line 208, in raise_
    raise exception
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\orm\session.py", line 3483, in _flush
    flush_context.execute()
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\orm\unitofwork.py", line 456, in execute
    rec.execute(self)
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\orm\unitofwork.py", line 630, in execute
    util.preloaded.orm_persistence.save_obj(
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\orm\persistence.py", line 245, in save_obj
    _emit_insert_statements(
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\orm\persistence.py", line 1238, in _emit_insert_statements
    result = connection._execute_20(
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\engine\base.py", line 1631, in _execute_20
    return meth(self, args_10style, kwargs_10style, execution_options)
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\sql\elements.py", line 325, in _execute_on_connection
    return connection._execute_clauseelement(
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\engine\base.py", line 1498, in _execute_clauseelement
    ret = self._execute_context(
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\engine\base.py", line 1862, in _execute_context
    self._handle_dbapi_exception(
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\engine\base.py", line 2043, in _handle_dbapi_exception
    util.raise_(
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\util\compat.py", line 208, in raise_
    raise exception
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\engine\base.py", line 1819, in _execute_context
    self.dialect.do_execute(
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\engine\default.py", line 732, in do_execute
    cursor.execute(statement, parameters)
sqlalchemy.exc.ProgrammingError: (psycopg2.errors.UndefinedTable) relation "clientes" does not exist
LINE 1: INSERT INTO clientes (nombre, documento) VALUES ('Marcos', '...
                    ^

[SQL: INSERT INTO clientes (nombre, documento) VALUES (%(nombre)s, %(documento)s) RETURNING clientes.id]
[parameters: {'nombre': 'Marcos', 'documento': '38123456'}]
(Background on this error at: https://sqlalche.me/e/14/f405)
Traceback (most recent call last):
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\engine\base.py", line 1819, in _execute_context
    self.dialect.do_execute(
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\engine\default.py", line 732, in do_execute
    cursor.execute(statement, parameters)
psycopg2.errors.DatatypeMismatch: foreign key constraint "facturas_client_id_fkey" cannot be implemented
DETAIL:  Key columns "client_id" and "id" are of incompatible types: character varying and integer.


The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\frand.LAPTOP-P3HHCD9I\Desktop\Fran\Curso Python\Proyecto fin\main.py", line 78, in <module>
    db.Base.metadata.create_all(db.engine)
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\sql\schema.py", line 4888, in create_all
    bind._run_ddl_visitor(
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\engine\base.py", line 3147, in _run_ddl_visitor
    conn._run_ddl_visitor(visitorcallable, element, **kwargs)
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\engine\base.py", line 2130, in _run_ddl_visitor
    visitorcallable(self.dialect, self, **kwargs).traverse_single(element)
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\sql\visitors.py", line 524, in traverse_single
    return meth(obj, **kw)
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\sql\ddl.py", line 851, in visit_metadata
    self.traverse_single(
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\sql\visitors.py", line 524, in traverse_single
    return meth(obj, **kw)
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\sql\ddl.py", line 895, in visit_table
    self.connection.execute(
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\engine\base.py", line 1306, in execute
    return meth(self, multiparams, params, _EMPTY_EXECUTION_OPTS)
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\sql\ddl.py", line 80, in _execute_on_connection
    return connection._execute_ddl(
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\engine\base.py", line 1398, in _execute_ddl
    ret = self._execute_context(
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\engine\base.py", line 1862, in _execute_context
    self._handle_dbapi_exception(
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\engine\base.py", line 2043, in _handle_dbapi_exception
    util.raise_(
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\util\compat.py", line 208, in raise_
    raise exception
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\engine\base.py", line 1819, in _execute_context
    self.dialect.do_execute(
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\engine\default.py", line 732, in do_execute
    cursor.execute(statement, parameters)
sqlalchemy.exc.ProgrammingError: (psycopg2.errors.DatatypeMismatch) foreign key constraint "facturas_client_id_fkey" cannot be implemented
DETAIL:  Key columns "client_id" and "id" are of incompatible types: character varying and integer.

[SQL: 
CREATE TABLE facturas (
	id SERIAL NOT NULL, 
	numero VARCHAR NOT NULL, 
	client_id VARCHAR, 
	PRIMARY KEY (id), 
	FOREIGN KEY(client_id) REFERENCES clientes (id)
)

]
(Background on this error at: https://sqlalche.me/e/14/f405)
Traceback (most recent call last):
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\engine\base.py", line 1819, in _execute_context
    self.dialect.do_execute(
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\engine\default.py", line 732, in do_execute
    cursor.execute(statement, parameters)
psycopg2.errors.DatatypeMismatch: foreign key constraint "facturas_client_id_fkey" cannot be implemented
DETAIL:  Key columns "client_id" and "id" are of incompatible types: character varying and integer.


The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\frand.LAPTOP-P3HHCD9I\Desktop\Fran\Curso Python\Proyecto fin\main.py", line 78, in <module>
    db.Base.metadata.create_all(db.engine)
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\sql\schema.py", line 4888, in create_all
    bind._run_ddl_visitor(
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\engine\base.py", line 3147, in _run_ddl_visitor
    conn._run_ddl_visitor(visitorcallable, element, **kwargs)
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\engine\base.py", line 2130, in _run_ddl_visitor
    visitorcallable(self.dialect, self, **kwargs).traverse_single(element)
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\sql\visitors.py", line 524, in traverse_single
    return meth(obj, **kw)
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\sql\ddl.py", line 851, in visit_metadata
    self.traverse_single(
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\sql\visitors.py", line 524, in traverse_single
    return meth(obj, **kw)
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\sql\ddl.py", line 895, in visit_table
    self.connection.execute(
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\engine\base.py", line 1306, in execute
    return meth(self, multiparams, params, _EMPTY_EXECUTION_OPTS)
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\sql\ddl.py", line 80, in _execute_on_connection
    return connection._execute_ddl(
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\engine\base.py", line 1398, in _execute_ddl
    ret = self._execute_context(
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\engine\base.py", line 1862, in _execute_context
    self._handle_dbapi_exception(
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\engine\base.py", line 2043, in _handle_dbapi_exception
    util.raise_(
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\util\compat.py", line 208, in raise_
    raise exception
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\engine\base.py", line 1819, in _execute_context
    self.dialect.do_execute(
  File "C:\Users\frand.LAPTOP-P3HHCD9I\.virtualenvs\Proyecto_fin-hXAYv8Iq\lib\site-packages\sqlalchemy\engine\default.py", line 732, in do_execute
    cursor.execute(statement, parameters)
sqlalchemy.exc.ProgrammingError: (psycopg2.errors.DatatypeMismatch) foreign key constraint "facturas_client_id_fkey" cannot be implemented
DETAIL:  Key columns "client_id" and "id" are of incompatible types: character varying and integer.

[SQL: 
CREATE TABLE facturas (
	id SERIAL NOT NULL, 
	numero VARCHAR NOT NULL, 
	client_id VARCHAR, 
	PRIMARY KEY (id), 
	FOREIGN KEY(client_id) REFERENCES clientes (id)
)

]
(Background on this error at: https://sqlalche.me/e/14/f405)
