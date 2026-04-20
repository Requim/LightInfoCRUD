from pydantic import BaseModel

class LightBase(BaseModel):
    brand: str
    model: str
    power: int
    color_temp: int

class LightCreate(LightBase):
    pass

class LightResponse(LightBase):
    id: int
    class Config:
        from_attributes = True