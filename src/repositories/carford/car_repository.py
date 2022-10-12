# Standard
from typing import List, NoReturn

# Local
from src.core.repositories.carford.i_car_repository import ICarCarfordRepository
from src.domain.models.carford.car_model import CarModel
from src.repositories.carford.base_repository import BaseCarfordRepository


class CarCarfordRepository(ICarCarfordRepository, BaseCarfordRepository):
    @classmethod
    def get_all_cars(cls) -> List[CarModel]:
        cars = cls.session.query(CarModel).all()

        return cars

    @classmethod
    def get_car_by_id(cls, car_id: int) -> CarModel:
        car = cls.session.query(CarModel).get(car_id)

        return car

    @classmethod
    def get_cars_by_client_id(cls, client_id: int) -> List[CarModel]:
        cars = cls.session.query(CarModel).filter(CarModel.client_id == client_id).all()

        return cars

    @classmethod
    def create_car(cls, car: CarModel) -> NoReturn:
        cls.session.add(car)
        cls.session.commit()

    @classmethod
    def delete_car_by_id(cls, car_id: int) -> NoReturn:
        cls.session.query(CarModel).filter(CarModel.id == car_id).delete()
        cls.session.commit()

    @classmethod
    def delete_car_by_client_id(cls, client_id: int) -> NoReturn:
        cls.session.query(CarModel).filter(CarModel.client_id == client_id).delete()
        cls.session.commit()
