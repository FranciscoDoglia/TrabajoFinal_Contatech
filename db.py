from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import psycopg2


engine = create_engine('postgresql://lknvayullpsvnj:d0c1fd3a599e7797a276a6e8b51d6e5215a41009cfc8b19b21aa2f26c2ca3c36@ec2-52-71-23-11.compute-1.amazonaws.com:5432/dbi1756bb2od2k')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()




