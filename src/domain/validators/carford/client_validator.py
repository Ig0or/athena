# Third Party
from pydantic import BaseModel, EmailStr, Extra


class ClientValidator(BaseModel):
    email: EmailStr
    sale_opportunity: bool

    class Config:
        extra = Extra.forbid
