
import psycopg2

t_host = "ec2-52-71-23-11.compute-1.amazonaws.com"
t_port = "5432" # default Postgres port
t_dbname = "dbi1756bb2od2k"
t_name_user = "lknvayullpsvnj"
t_password = "d0c1fd3a599e7797a276a6e8b51d6e5215a41009cfc8b19b21aa2f26c2ca3c36"
db_conn = psycopg2.connect(host=t_host, port=t_port, dbname=t_dbname, user=t_name_user, password=t_password)
db_cursor = db_conn.cursor()

def update_db():
    t_current_table = 'clientes'
    s = "ALTER TABLE clientes ADD documento varchar"
    db_cursor.execute(s)
    db_conn.commit()

update_db()