# Standard
from abc import abstractmethod
from typing import NoReturn

# Local
from src.domain.models.carford.client_model import ClientModel


class IClientCarfordService:
    @staticmethod
    @abstractmethod
    def verify_if_client_exists_by_id(client_id: int) -> ClientModel:
        pass

    @staticmethod
    @abstractmethod
    def verify_client_sale_opportunity(client_id: int) -> NoReturn:
        pass

    @staticmethod
    @abstractmethod
    def verify_client_cars_quantity(client_id: int) -> NoReturn:
        pass

    @staticmethod
    @abstractmethod
    def get_all_clients() -> list:
        pass

    @staticmethod
    @abstractmethod
    def get_client_by_id(client_id: int) -> dict:
        pass

    @staticmethod
    @abstractmethod
    def create_client(new_client: dict) -> NoReturn:
        pass

    @staticmethod
    @abstractmethod
    def update_client_by_id(client_changes: dict, client_id: int) -> NoReturn:
        pass

    @staticmethod
    @abstractmethod
    def delete_client_by_id(client_id: int) -> NoReturn:
        pass
