from sqlalchemy.orm import relationship
import db
from sqlalchemy import Column, String, Integer, ForeignKey


class Cliente(db.Base):
    __tablename__ = 'cliente'
    # tipo_iva = ['RI', 'MONO', 'CF', 'EXE']
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    documento = Column(String(13), nullable=False)
    fac_rel = relationship('Factura', backref="parent", lazy=True)

    def __init__(self, nombre: str, documento: str):
        super(Cliente, self).__init__()
        self.nombre = nombre
        self.documento = documento

    def __str__(self):
        return f'Cliente: {self.id}, {self.nombre}, {self.documento}'

    def __repr__(self):
        return f'Cliente: {self.id}, {self.nombre}, {self.documento}'


class Factura(db.Base): #Podría guardarlas en la base de datos también
    __tablename__ = 'factura'
    id = Column(Integer, primary_key=True)
    numero = Column(String, nullable=False)
    cliente_id = Column(Integer, ForeignKey('cliente.id'))
#Agregar que la columna numero no puede repetirse para el mismo cliente_id

    def __init__(self, numero: str):
        super(Factura, self).__init__()
        self.numero = numero

