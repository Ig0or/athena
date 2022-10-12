# Third Party
from pydantic import BaseModel, Extra

# Local
from src.domain.enums.carford.enums import CarColors, CarModels


class CarValidator(BaseModel):
    color: CarColors
    model: CarModels
    client_id: int

    class Config:
        extra = Extra.forbid
