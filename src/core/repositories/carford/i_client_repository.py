# Standard
from abc import abstractmethod
from typing import List, NoReturn

# Local
from src.domain.models.carford.client_model import ClientModel


class IClientCarfordRepository:
    @classmethod
    @abstractmethod
    def get_all_clients(cls) -> List[ClientModel]:
        pass

    @classmethod
    @abstractmethod
    def get_client_by_id(cls, client_id: int) -> ClientModel:
        pass

    @classmethod
    @abstractmethod
    def get_client_by_email(cls, client_email: str) -> ClientModel:
        pass

    @classmethod
    @abstractmethod
    def create_client(cls, client: ClientModel) -> NoReturn:
        pass

    @classmethod
    @abstractmethod
    def update_client_by_id(
        cls, updated_client: ClientModel, client_id: int
    ) -> NoReturn:
        pass

    @classmethod
    @abstractmethod
    def delete_client_by_id(cls, client_id: int) -> NoReturn:
        pass
