from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://kvjnzvxgogyvjy:800d850e3f7470a96a455b482fdbc78af897ae35be1448c5ca6fca3952c7eb56@ec2-54-198-213-75.compute-1.amazonaws.com:5432/dctt8pu7be6rlh')
#cambiar engine y ponerle el que genere en heroku
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
