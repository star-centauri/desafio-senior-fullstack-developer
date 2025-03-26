import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Leia a variável de ambiente; use valor padrão se não estiver definida
DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://user:password@localhost:5432/mydatabase")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()