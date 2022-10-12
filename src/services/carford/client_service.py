# Standard
from typing import NoReturn

# Local
from src.core.services.carford.i_client_service import IClientCarfordService
from src.domain.exceptions.carford.exceptions import (
    ClientAlreadyExists,
    ClientCarsLimitExceeded,
    ClientNotExists,
    ClientNotSaleOpportunity,
)
from src.domain.models.carford.client_model import ClientModel
from src.domain.validators.carford.client_validator import ClientValidator
from src.repositories.carford.car_repository import CarCarfordRepository
from src.repositories.carford.client_repository import ClientCarfordRepository


class ClientCarfordService(IClientCarfordService):
    @staticmethod
    def verify_if_client_exists_by_id(client_id: int) -> ClientModel:
        client = ClientCarfordRepository.get_client_by_id(client_id=client_id)

        if not client:
            raise ClientNotExists

        return client

    @staticmethod
    def verify_client_sale_opportunity(client_id: int) -> NoReturn:
        client = ClientCarfordRepository.get_client_by_id(client_id=client_id)

        if not client.sale_opportunity:
            raise ClientNotSaleOpportunity

    @staticmethod
    def verify_client_cars_quantity(client_id: int) -> NoReturn:
        cars = CarCarfordRepository.get_cars_by_client_id(client_id=client_id)

        if len(cars) >= 3:
            raise ClientCarsLimitExceeded

    @staticmethod
    def get_all_clients() -> list:
        clients = ClientCarfordRepository.get_all_clients()
        clients_dict_list = [client.to_dict() for client in clients]

        return clients_dict_list

    @staticmethod
    def get_client_by_id(client_id: int) -> dict:
        client = ClientCarfordService.verify_if_client_exists_by_id(client_id=client_id)
        client_dict = client.to_dict()

        client_cars = CarCarfordRepository.get_cars_by_client_id(client_id=client_id)
        cars_dict_list = [car.to_dict() for car in client_cars]

        client_dict.update({"cars": cars_dict_list})

        return client_dict

    @staticmethod
    def create_client(new_client: dict) -> NoReturn:
        client_validator = ClientValidator(**new_client)

        client = ClientCarfordRepository.get_client_by_email(
            client_email=client_validator.email
        )

        if client:
            raise ClientAlreadyExists

        client_model = ClientModel(
            email=client_validator.email,
            sale_opportunity=client_validator.sale_opportunity,
        )
        ClientCarfordRepository.create_client(client=client_model)

    @staticmethod
    def update_client_by_id(client_changes: dict, client_id: int) -> NoReturn:
        client_validator = ClientValidator(**client_changes)

        ClientCarfordService.verify_if_client_exists_by_id(client_id=client_id)

        client_model = ClientModel(
            email=client_validator.email,
            sale_opportunity=client_validator.sale_opportunity,
        )
        ClientCarfordRepository.update_client_by_id(
            updated_client=client_model, client_id=client_id
        )

    @staticmethod
    def delete_client_by_id(client_id: int) -> NoReturn:
        ClientCarfordService.verify_if_client_exists_by_id(client_id=client_id)

        ClientCarfordRepository.delete_client_by_id(client_id=client_id)
        CarCarfordRepository.delete_car_by_client_id(client_id=client_id)
