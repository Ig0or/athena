# Third Party
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class ClientModel(Base):
    __tablename__ = "CLIENT"

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    email = Column(String(30), nullable=False)
    sale_opportunity = Column(Boolean, nullable=False)

    def to_dict(self) -> dict:
        client_dict = {
            "id": self.id,
            "email": self.email,
            "sale_opportunity": self.sale_opportunity,
        }

        return client_dict
