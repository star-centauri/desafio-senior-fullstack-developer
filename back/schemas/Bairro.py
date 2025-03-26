from pydantic import BaseModel, PositiveInt

class BairroSchema(BaseModel):
    id: PositiveInt
    name: str

    class Config:
        orm_mode = True