# Standard
from typing import NoReturn

# Local
from src.domain.exceptions.carford.exceptions import (
    CarNotExists,
)
from src.domain.models.carford.car_model import CarModel
from src.domain.validators.carford.car_validator import CarValidator
from src.repositories.carford.car_repository import CarCarfordRepository
from src.services.carford.client_service import ClientCarfordService


class CarCarfordService:
    @staticmethod
    def _verify_if_car_exists_by_id(car_id: int) -> CarModel:
        car = CarCarfordRepository.get_car_by_id(car_id=car_id)

        if not car:
            raise CarNotExists

        return car

    @staticmethod
    def get_all_cars() -> list:
        cars = CarCarfordRepository.get_all_cars()
        cars_dict_list = [car.to_dict() for car in cars]

        return cars_dict_list

    @staticmethod
    def get_car_by_id(car_id: int) -> dict:
        car = CarCarfordService._verify_if_car_exists_by_id(car_id=car_id)
        car_dict = car.to_dict()

        return car_dict

    @staticmethod
    def create_car(new_car: dict) -> NoReturn:
        car_validator = CarValidator(**new_car)

        ClientCarfordService.verify_if_client_exists_by_id(
            client_id=car_validator.client_id
        )
        ClientCarfordService.verify_client_sale_opportunity(
            client_id=car_validator.client_id
        )
        ClientCarfordService.verify_client_cars_quantity(
            client_id=car_validator.client_id
        )

        car_model = CarModel(
            color=car_validator.color,
            model=car_validator.model,
            client_id=car_validator.client_id,
        )
        CarCarfordRepository.create_car(car=car_model)

    @staticmethod
    def delete_car_by_id(car_id: int) -> NoReturn:
        CarCarfordService._verify_if_car_exists_by_id(car_id=car_id)

        CarCarfordRepository.delete_car_by_id(car_id=car_id)
