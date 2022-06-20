from sqlalchemy.orm import relationship

import db
from sqlalchemy import Column, String, Integer, ForeignKey
from IvaExc import IvaExc


class Cliente(db.Base):
    __tablename__ = 'clientes'
    # tipo_iva = ['RI', 'MONO', 'CF', 'EXE']

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    documento = Column(String, nullable=False)

    def __init__(self, nombre: str, documento: str, t_iva: str):
        self.nombre = nombre
        self.documento = documento
        # self.t_iva = t_iva  #obtener desde Flask o Input

    def __validar_iva(self):
        #if t_iva pertenece a tipo_iva, true; else = error
        pass

class Factura(db.Base): #Podría guardarlas en la base de datos también
    __tablename__ = 'facturas'
    id = Column(Integer, primary_key=True)
    cliente_id = Column(String, ForeignKey(Cliente.id))
    # cliente_name = Column(String, ForeignKey(clientes.nombre)) Falta todavia crear la relacion y emprolijar esto
    # cliente_documento = Column(String, ForeignKey(clientes.documento))
    cliente = relationship(Cliente, backref= 'facturas')

    # def __init__(self, p_venta: str,numero: str,cliente: Cliente,fecha: str ,netog: float,alic_iva: float ):
    #     self.p_venta = p_venta
    #     self.numero = numero
    #     self.cliente = cliente
    #     self.fecha = fecha
    #     self.netog = netog
    #     self.alic_iva = alic_iva
    def __init__(self, numero: str):
        self.numero = numero

    def __devolver_total(self) -> float:
        total = self.netog * (1 + self.alic_iva)
        return total

    @property
    def total(self):
        return self.__devolver_total()

    def print_fc(self):     # A partir de tomar una plantilla modelo de factura
        print(self.cliente.nombre)
        print(self.cliente.documento)
        # print(self.cliente.tipo_iva)
        # print(self.total)
        pass
