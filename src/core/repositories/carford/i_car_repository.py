# Standard
from abc import abstractmethod
from typing import List, NoReturn

# Local
from src.domain.models.carford.car_model import CarModel


class ICarCarfordRepository:
    @classmethod
    @abstractmethod
    def get_all_cars(cls) -> List[CarModel]:
        pass

    @classmethod
    @abstractmethod
    def get_car_by_id(cls, car_id: int) -> CarModel:
        pass

    @classmethod
    @abstractmethod
    def get_cars_by_client_id(cls, client_id: int) -> List[CarModel]:
        pass

    @classmethod
    @abstractmethod
    def create_car(cls, car: CarModel) -> NoReturn:
        pass

    @classmethod
    @abstractmethod
    def delete_car_by_id(cls, car_id: int) -> NoReturn:
        pass

    @classmethod
    @abstractmethod
    def delete_car_by_client_id(cls, client_id: int) -> NoReturn:
        pass
