from pydantic import BaseModel, PositiveInt
from schemas.Categoria import CategoriaSchema
from schemas.Bairro import BairroSchema
from schemas.Status import StatuSchema

class SolicitacaoSchema(BaseModel):
    id: PositiveInt
    title: str
    describe: str
    category: CategoriaSchema
    bairro: BairroSchema
    status: StatuSchema

    class Config:
        orm_mode = True

class CreateSchema(BaseModel):
    title: str
    describe: str
    category_id: PositiveInt
    bairro_id: PositiveInt
    status_id: PositiveInt

    class Config:
        orm_mode = True

class UpdateSchema(BaseModel):
    describe: str
    category_id: PositiveInt
    status_id: PositiveInt

    class Config:
        orm_mode = True