# Standard
from typing import List, NoReturn

# Local
from src.domain.models.carford.client_model import ClientModel
from src.repositories.carford.base_repository import BaseCarfordRepository


class ClientCarfordRepository(BaseCarfordRepository):
    @classmethod
    def get_all_clients(cls) -> List[ClientModel]:
        clients = cls.session.query(ClientModel).all()

        return clients

    @classmethod
    def get_client_by_id(cls, client_id: int) -> ClientModel:
        client = cls.session.query(ClientModel).get(client_id)

        return client

    @classmethod
    def get_client_by_email(cls, client_email: str) -> ClientModel:
        client = (
            cls.session.query(ClientModel)
            .filter(ClientModel.email == client_email)
            .all()
        )

        return client

    @classmethod
    def create_client(cls, client: ClientModel) -> NoReturn:
        cls.session.add(client)
        cls.session.commit()

    @classmethod
    def update_client_by_id(
        cls, updated_client: ClientModel, client_id: int
    ) -> NoReturn:
        cls.session.query(ClientModel).filter(ClientModel.id == client_id).update(
            {
                ClientModel.email: updated_client.email,
                ClientModel.sale_opportunity: updated_client.sale_opportunity,
            }
        )
        cls.session.commit()

    @classmethod
    def delete_client_by_id(cls, client_id: int) -> NoReturn:
        cls.session.query(ClientModel).filter(ClientModel.id == client_id).delete()
        cls.session.commit()
