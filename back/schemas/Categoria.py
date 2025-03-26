from pydantic import BaseModel, PositiveInt

class CategoriaSchema(BaseModel):
    id: PositiveInt
    name: str

    class Config:
        orm_mode = True