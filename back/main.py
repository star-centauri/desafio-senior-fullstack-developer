from typing import Union
from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from db.config import engine, SessionLocal, Base
from db.models import Status, Bairro, Categoria

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    db: Session = SessionLocal()
    # TODO: refatorar essa parte
    try:
        # Gravar status default
        status_iniciais = ["pendente", "andamento", "concluído"]
        exists_status = db.query(Status).filter(Status.name.in_(status_iniciais)).all()
        map_status = {s.name for s in exists_status}
        for name in status_iniciais:
            if name not in map_status:
                db.add(Status(name=name))

        # Gravar alguns bairros default para testar
        bairro_iniciais = ["São Cristovão", "Tijuca", "Curricia", "Pechincha", "Saens Pena", "Copacabana"]
        exists_bairro = db.query(Bairro).filter(Bairro.name.in_(bairro_iniciais)).all()
        map_bairro = { b.name for b in exists_bairro }
        for name in bairro_iniciais:
            if name not in map_bairro:
                db.add(Bairro(name=name))

        # Gravar algumas categorias para testar
        categoria_iniciais = ["conserto", "instalação", "coleta"]
        exists_categoria = db.query(Categoria).filter(Bairro.name.in_(categoria_iniciais)).all()
        map_categoria = { c.name for c in exists_categoria }
        for name in categoria_iniciais:
            if name not in map_categoria:
                db.add(Categoria(name=name))
        
        db.commit()
    except ValueError as err:
        raise f"Erro na conexão com o database: {err}"
    finally:
        db.close()

app = FastAPI(lifespan=lifespan)

# Para resolver problemas de CORS
origins = [
    "http://localhost:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,         
    allow_credentials=True,
    allow_methods=["*"],            
    allow_headers=["*"],          
)

@app.get("/solicitacoes")
def read_root():
    return {"Hello": "World"}


@app.get("/solicitacoes/{id}")
def read_item(id: int, q: Union[str, None] = None):
    return {"id": id, "q": q}

@app.post("/solicitacao")
def create_item():
    return None

@app.patch("/solicitacoes/{id}")
def update_item():
    return None