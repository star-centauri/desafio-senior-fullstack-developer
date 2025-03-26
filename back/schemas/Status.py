from pydantic import BaseModel, PositiveInt

class StatuSchema(BaseModel):
    id: PositiveInt
    name: str

    class Config:
        orm_mode = True