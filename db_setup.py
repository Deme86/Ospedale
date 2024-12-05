from sqlalchemy import create_engine
from models import Base
from config.config import DATABASE_URI

def setup_database():
    engine = create_engine(DATABASE_URI)
    Base.metadata.create_all(engine)
    print("Tabelle create con successo!")

if __name__ == "__main__":
    setup_database()
