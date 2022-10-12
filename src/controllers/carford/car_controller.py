# Third Party
from http import HTTPStatus

# Local
from src.domain.exceptions.carford.exceptions import (
    CarNotExists,
    ClientCarsLimitExceeded,
    ClientNotExists,
    ClientNotSaleOpportunity,
)
from src.services.carford.car_service import CarCarfordService


class CarCarfordController:
    @staticmethod
    def get_all_cars() -> dict:
        try:
            clients = CarCarfordService.get_all_cars()
            response = {"success": True, "result": clients, "code": HTTPStatus.OK}

        except Exception as exception:
            response = {
                "success": False,
                "message": "Error to get cars",
                "code": HTTPStatus.INTERNAL_SERVER_ERROR,
            }

        return response

    @staticmethod
    def get_car_by_id(car_id: int) -> dict:
        try:
            car = CarCarfordService.get_car_by_id(car_id=car_id)
            response = {"success": True, "result": car, "code": HTTPStatus.OK}

        except CarNotExists as exception:
            response = {
                "success": False,
                "message": "There isn't a car with this id",
                "code": HTTPStatus.BAD_REQUEST,
            }

        except Exception as exception:
            response = {
                "success": False,
                "message": "Error to get this car",
                "code": HTTPStatus.INTERNAL_SERVER_ERROR,
            }

        return response

    @staticmethod
    def create_car(request_body: dict) -> dict:
        try:
            CarCarfordService.create_car(new_car=request_body)
            response = {
                "success": True,
                "message": "This car was inserted successfully",
                "code": HTTPStatus.CREATED,
            }

        except ValueError as exception:
            response = {
                "success": False,
                "message": "Invalid parameters",
                "code": HTTPStatus.BAD_REQUEST,
            }

        except ClientNotExists as exception:
            response = {
                "success": False,
                "message": "There isn't a client with this id",
                "code": HTTPStatus.BAD_REQUEST,
            }

        except ClientNotSaleOpportunity as exception:
            response = {
                "success": False,
                "message": "This client isn't open to a sale opportunity",
                "code": HTTPStatus.BAD_REQUEST,
            }

        except ClientCarsLimitExceeded as exception:
            response = {
                "success": False,
                "message": "This client already exceeded their limit of cars quantity",
                "code": HTTPStatus.BAD_REQUEST,
            }

        except Exception as exception:
            response = {
                "success": False,
                "message": "Error to create a car",
                "code": HTTPStatus.INTERNAL_SERVER_ERROR,
            }

        return response

    @staticmethod
    def delete_car_by_id(car_id: int) -> dict:
        try:
            CarCarfordService.delete_car_by_id(car_id=car_id)
            response = {
                "success": True,
                "message": "This car was delete successfully",
                "code": HTTPStatus.OK,
            }

        except CarNotExists as exception:
            response = {
                "success": False,
                "message": "There isn't a car with this id",
                "code": HTTPStatus.BAD_REQUEST,
            }

        except Exception as exception:
            response = {
                "success": False,
                "message": "Error to delete this car",
                "code": HTTPStatus.INTERNAL_SERVER_ERROR,
            }

        return response
