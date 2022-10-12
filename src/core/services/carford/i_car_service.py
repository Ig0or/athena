# Standard
from abc import abstractmethod
from typing import NoReturn

# Local
from src.domain.models.carford.car_model import CarModel


class ICarCarfordService:
    @staticmethod
    @abstractmethod
    def _verify_if_car_exists_by_id(car_id: int) -> CarModel:
        pass

    @staticmethod
    @abstractmethod
    def get_all_cars() -> list:
        pass

    @staticmethod
    @abstractmethod
    def get_car_by_id(car_id: int) -> dict:
        pass

    @staticmethod
    @abstractmethod
    def create_car(new_car: dict) -> NoReturn:
        pass

    @staticmethod
    @abstractmethod
    def delete_car_by_id(car_id: int) -> NoReturn:
        pass
