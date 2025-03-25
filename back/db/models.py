from sqlalchemy import Column, Integer, String, Text, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship
from back.db.config import Base

class Status(Base):
    __tablename__ = "tb_status"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

class Bairro(Base):
    __tablename__ = "tb_bairro"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

class Categoria(Base):
    __tablename__ = "tb_categoria"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

class Solicitacao(Base):
    __tablename__ = "tb_solicitacao"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    describe = Column(Text, nullable=False)

    # Relacionamento com a tabela categoria
    category_id = Column(Integer, ForeignKey("tb_categoria.id"), nullable=False)
    category = relationship("Categoria")

    # Relacionamento com a tabela bairro
    bairro_id = Column(Integer, ForeignKey("tb_bairro.id"), nullable=False)
    bairro = relationship("Bairro")
    
    # Relacionamento com a tabela status
    status_id = Column(Integer, ForeignKey("tb_status.id"), nullable=False)
    status = relationship("Status")

    # Armazenamento de imagem
    photo = Column(LargeBinary)
