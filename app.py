from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Paziente
from config.config import DATABASE_URI

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

def inserisci_paziente(nome, data_nascita, indirizzo, telefono, email):
    paziente = Paziente(
        nome=nome,
        data_nascita=data_nascita,
        indirizzo=indirizzo,
        telefono=telefono,
        email=email
    )
    session.add(paziente)
    session.commit()
    print(f"Paziente {nome} aggiunto con successo!")

def leggi_pazienti():
    pazienti = session.query(Paziente).all()
    for p in pazienti:
        print(f"{p.nome}, {p.data_nascita}, {p.email}")

if __name__ == "__main__":
    # Inserire un paziente
    inserisci_paziente(
        nome="Mario Rossi",
        data_nascita="1980-01-01",
        indirizzo="Via Roma 10",
        telefono="3331234567",
        email="mario.rossi@example.com"
    )
    # Leggere tutti i pazienti
    leggi_pazienti()
