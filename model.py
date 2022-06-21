from sqlalchemy.orm import relationship
import db
from sqlalchemy import Column, String, Integer, ForeignKey
# from IvaExc import IvaExc


class Cliente(db.Base):
    __tablename__ = 'clientes'
    # tipo_iva = ['RI', 'MONO', 'CF', 'EXE']
    id = Column(String, primary_key=True) #suplante el ID que en realidad deberpia ser un num d ebase de datos
    nombre = Column(String, nullable=False)
    # documento = Column(String, nullable=False)
    # comprobantes = relationship('Factura')

    def __init__(self, id ,nombre: str):
        super(Cliente, self).__init__()
        self.id = id
        self.nombre = nombre
        # self.documento = documento
        # self.t_iva = t_iva  #obtener desde Flask o Input
    def consulta(self):
        consulta = db.session.query(Cliente).all()
        print(consulta)
    # def __validar_iva(self):
    #     #if t_iva pertenece a tipo_iva, true; else = error
    #     pass

# class Factura(db.Base): #Podría guardarlas en la base de datos también
#     __tablename__ = 'facturas'
#     id = Column(Integer, primary_key=True)
#     client_id = Column(String, ForeignKey('clientes.id'))
#     client_name = Column(String, ForeignKey('clientes.nombre'))
#     # client_documento = Column(String, ForeignKey(''))
#     cliente = relationship('Cliente', backref= 'facturas')
#
#     def __init__(self, id: str):
#         super(Factura, self).__init__()
#         self.id = id



    # def __devolver_total(self) -> float:
    #     total = self.netog * (1 + self.alic_iva)
    #     return total

    # @property
    # def total(self):
    #     return self.__devolver_total()

    # def print_fc(self):     # A partir de tomar una plantilla modelo de factura
    #     print(self.client_name)
    #     print(self.client_documento)
    #     # print(self.cliente.tipo_iva)
    #     # print(self.total)
    #     pass

