from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Date,
    Float,
    ForeignKey,
    DECIMAL,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

# Definizione delle tabelle

class Paziente(Base):
    __tablename__ = 'pazienti'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    data_nascita = Column(Date, nullable=False)
    indirizzo = Column(String(200))
    telefono = Column(String(15))
    email = Column(String(100), unique=True)
    visite = relationship("Visita", back_populates="paziente")
    ricoveri = relationship("Ricovero", back_populates="paziente")
    pagamenti = relationship("Pagamento", back_populates="paziente")

class Medico(Base):
    __tablename__ = 'medici'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    specializzazione = Column(String(100))
    reparto = Column(String(100))
    turno = Column(String(50))
    visite = relationship("Visita", back_populates="medico")
    prescrizioni = relationship("Prescrizione", back_populates="medico")

class Visita(Base):
    __tablename__ = 'visite'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(Date, nullable=False)
    diagnosi = Column(String(255))
    medico_id = Column(Integer, ForeignKey('medici.ID'), nullable=False)
    paziente_id = Column(Integer, ForeignKey('pazienti.ID'), nullable=False)
    prescrizioni = relationship("Prescrizione", back_populates="visita")
    pagamenti = relationship("Pagamento", back_populates="visita")
    medico = relationship("Medico", back_populates="visite")
    paziente = relationship("Paziente", back_populates="visite")

class Ricovero(Base):
    __tablename__ = 'ricoveri'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    data_ingresso = Column(Date, nullable=False)
    data_dimissione = Column(Date)
    reparto_id = Column(Integer, ForeignKey('reparti.ID'), nullable=False)
    paziente_id = Column(Integer, ForeignKey('pazienti.ID'), nullable=False)
    reparto = relationship("Reparto", back_populates="ricoveri")
    paziente = relationship("Paziente", back_populates="ricoveri")
    pagamenti = relationship("Pagamento", back_populates="ricovero")

class Prescrizione(Base):
    __tablename__ = 'prescrizioni'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    data_prescrizione = Column(Date, nullable=False)
    medico_id = Column(Integer, ForeignKey('medici.ID'), nullable=False)
    visita_id = Column(Integer, ForeignKey('visite.ID'), nullable=False)
    farmaco_id = Column(Integer, ForeignKey('farmaci.ID'), nullable=False)
    medico = relationship("Medico", back_populates="prescrizioni")
    visita = relationship("Visita", back_populates="prescrizioni")
    farmaco = relationship("Farmaco", back_populates="prescrizioni")

class Farmaco(Base):
    __tablename__ = 'farmaci'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    nome_farmaco = Column(String(100), nullable=False)
    dosaggio = Column(String(50))
    prescrizioni = relationship("Prescrizione", back_populates="farmaco")

class Pagamento(Base):
    __tablename__ = 'pagamenti'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    data_pagamento = Column(Date, nullable=False)
    importo = Column(DECIMAL(10, 2), nullable=False)
    metodo_pagamento = Column(String(50))
    visita_id = Column(Integer, ForeignKey('visite.ID'))
    ricovero_id = Column(Integer, ForeignKey('ricoveri.ID'))
    paziente_id = Column(Integer, ForeignKey('pazienti.ID'), nullable=False)
    visita = relationship("Visita", back_populates="pagamenti")
    ricovero = relationship("Ricovero", back_populates="pagamenti")
    paziente = relationship("Paziente", back_populates="pagamenti")

class Reparto(Base):
    __tablename__ = 'reparti'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    nome_reparto = Column(String(100), nullable=False)
    medico_caporeparto = Column(String(100))
    posti_letto = Column(Integer)
    ricoveri = relationship("Ricovero", back_populates="reparto")
