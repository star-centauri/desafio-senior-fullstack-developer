from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from datetime import datetime

from db.config import engine, SessionLocal, Base, get_db
from db.models import Status, Bairro, Categoria, Solicitacao
from schemas.Solicitacao import SolicitacaoSchema, CreateSchema, UpdateSchema

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
        exists_categoria = db.query(Categoria).filter(Categoria.name.in_(categoria_iniciais)).all()
        map_categoria = { c.name for c in exists_categoria }
        for name in categoria_iniciais:
            if name not in map_categoria:
                db.add(Categoria(name=name))
        
        db.commit()
    except Exception as err:
        raise Exception(f"Erro na conexão com o database: {err}")
    finally:
        db.close()

    yield

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

@app.post("/solicitacoes", response_model=SolicitacaoSchema)
def create_item(solicitacao: CreateSchema, db: Session = Depends(get_db)):
    bairro = db.query(Bairro).filter(Bairro.id == solicitacao.bairro_id).first()
    status = db.query(Status).filter(Status.id == solicitacao.status_id).first()
    category = db.query(Categoria).filter(Categoria.id == solicitacao.category_id).first()

    if not bairro or not status or not category:
        raise HTTPException(status_code=400, detail="Não foi possível criar essa solicitação.")
    
    new_socilitacao = Solicitacao(
        title=solicitacao.title,
        describe=solicitacao.describe,
        data_create=datetime.now(),
        category_id=category.id,
        bairro_id=bairro.id,
        status_id=status.id
    )
    
    db.add(new_socilitacao)
    db.commit()
    db.refresh(new_socilitacao)

    return new_socilitacao

@app.get("/solicitacoes", response_model=List[SolicitacaoSchema])
def read_items(db: Session = Depends(get_db)):
    solicitacoes = db.query(Solicitacao).all()
    return solicitacoes


@app.get("/solicitacoes/{id}")
def read_item(id: int, db: Session = Depends(get_db)):
    solicitacao = db.query(Solicitacao).filter(Solicitacao.id == id).first()
    
    if not solicitacao:
        raise HTTPException(status_code=404, detail="Solicitação não encontrado")
    
    return solicitacao

@app.patch("/solicitacoes/{id}", response_model=SolicitacaoSchema)
def update_item(id: int, update: UpdateSchema, db: Session = Depends(get_db)):
    solicitacao = db.query(Solicitacao).filter(Solicitacao.id == id).first()
    
    if not solicitacao:
        raise HTTPException(status_code=404, detail="Solicitacao não encontrado para edição")
    
    status = db.query(Status).filter(Status.id == solicitacao.status_id).first()
    category = db.query(Categoria).filter(Categoria.id == solicitacao.category_id).first()

    if not status or not category:
        raise HTTPException(status_code=400, detail="Não foi possível editar essa solicitação.")
    
    solicitacao.describe = update.describe
    solicitacao.category_id = update.category_id
    solicitacao.status_id = update.status_id

    db.commit()
    db.refresh(solicitacao)
    
    return solicitacao