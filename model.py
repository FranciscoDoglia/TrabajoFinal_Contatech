from sqlalchemy.orm import relationship
import db
from sqlalchemy import Column, String, Integer, ForeignKey


class Cliente(db.Base):
    __tablename__ = 'clientes'
    # tipo_iva = ['RI', 'MONO', 'CF', 'EXE']
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    documento = Column(String(13), nullable=False)
    comprobantes = relationship('Factura', backref='client')

    def __init__(self, nombre: str, documento: str):
        super(Cliente, self).__init__()
        self.nombre = nombre
        self.documento = documento
        # self.t_iva = t_iva  #obtener desde Flask o Input

    def __str__(self):
        return f'Cliente: {self.id}, {self.nombre}, {self.documento}'

    def __repr__(self):
        return f'Cliente: {self.id}, {self.nombre}, {self.documento}'

    # def __validar_iva(self):
    #     #if t_iva pertenece a tipo_iva, true; else = error
    #     pass

class Factura(db.Base): #Podría guardarlas en la base de datos también
    __tablename__ = 'facturas'
    id = Column(Integer, primary_key=True)
    numero = Column(String, nullable=False)
    client_id = Column(String, ForeignKey('clientes.id'))
    # client_name = Column(String, ForeignKey('clientes.nombre'))
    # client_documento = Column(String, ForeignKey('clientes.documento'))
    # client_rel_id = relationship('Cliente', foreign_keys=[client_id])
    # client_rel_name = relationship('Cliente', foreign_keys=[client_name])
    # client_rel_document = relationship('Cliente', foreign_keys=[client_documento])

    def __init__(self, numero: str):
        super(Factura, self).__init__()
        self.numero = numero





