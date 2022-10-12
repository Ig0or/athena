# Third Party
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class CarModel(Base):
    __tablename__ = "CAR"

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    color = Column(String(15), nullable=False)
    model = Column(String(15), nullable=False)
    client_id = Column(Integer, nullable=False)

    def to_dict(self) -> dict:
        car_dict = {
            "id": self.id,
            "color": self.color,
            "model": self.model,
            "client_id": self.client_id,
        }

        return car_dict
