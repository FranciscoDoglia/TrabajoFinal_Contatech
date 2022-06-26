from sqlalchemy.orm import relationship
import db
from sqlalchemy import Column, String, Integer, ForeignKey


class Cliente(db.Base):
    __tablename__ = 'clientes'
    # tipo_iva = ['RI', 'MONO', 'CF', 'EXE']
    id = Column(Integer, primary_key=True) #suplante el ID que en realidad deberpia ser un num d ebase de datos
    nombre = Column(String, nullable=False)
    documento = Column(String, nullable=False)
    # comprobantes = relationship('Factura')

    def __init__(self, nombre: str, documento: str): #, documento: str):
        super(Cliente, self).__init__()
        self.nombre = nombre
        self.documento = documento
        # self.t_iva = t_iva  #obtener desde Flask o Input

    def __str__(self):
        return f'Cliente: {self.id}, {self.nombre}, {self.documento}'

    def __repr__(self):
        return f'Taks: {self.id}, {self.nombre}, {self.documento}'
