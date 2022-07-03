from sqlalchemy.orm import relationship
import db
from sqlalchemy import Column, String, Integer, ForeignKey, Float


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
    neto_gravado = Column(Float, nullable=False)
    alic_iva = Column(Float, nullable=True)
    cliente_id = Column(Integer, ForeignKey('cliente.id'))
#Agregar que la columna numero no puede repetirse para el mismo cliente_id

    def __init__(self, numero: str, neto_gravado: float, alic_iva: float):
        super(Factura, self).__init__()
        self.numero = numero
        self.neto_gravado = neto_gravado
        self.alic_iva = alic_iva

    def __devolver_total(self) -> float:
        total = self.neto_gravado * (1 + (self.alic_iva/100))
        return total

    @property
    def total(self):
        return self.__devolver_total()

    def __devolver_iva(self) -> float:
        iva = self.neto_gravado *  (self.alic_iva / 100)
        return iva

    @property
    def iva(self):
        return self.__devolver_iva()


    # def print_fc(self):     # A partir de tomar una plantilla modelo de factura
    #     print(self.parent.nombre)
    #     print(self.parent.documento)
    #     print(self.total - self.iva)
    #     print(self.iva)
    #     print(self.total)
    #     pass


