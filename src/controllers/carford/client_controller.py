# Third Party
from http import HTTPStatus

# Local
from src.domain.exceptions.carford.exceptions import (
    ClientAlreadyExists,
    ClientNotExists,
)
from src.services.carford.client_service import ClientCarfordService


class ClientCarfordController:
    @staticmethod
    def get_all_clients() -> dict:
        try:
            clients = ClientCarfordService.get_all_clients()
            response = {"success": True, "result": clients, "code": HTTPStatus.OK}

        except Exception as exception:
            response = {
                "success": False,
                "message": "Error to get clients",
                "code": HTTPStatus.INTERNAL_SERVER_ERROR,
            }

        return response

    @staticmethod
    def get_client_by_id(client_id: int) -> dict:
        try:
            client = ClientCarfordService.get_client_by_id(client_id=client_id)
            response = {"success": True, "result": client, "code": HTTPStatus.OK}

        except ClientNotExists as exception:
            response = {
                "success": False,
                "message": "There isn't a client with this id",
                "code": HTTPStatus.BAD_REQUEST,
            }

        except Exception as exception:
            response = {
                "success": False,
                "message": "Error to get this client",
                "code": HTTPStatus.INTERNAL_SERVER_ERROR,
            }

        return response

    @staticmethod
    def create_client(request_body: dict) -> dict:
        try:
            ClientCarfordService.create_client(new_client=request_body)
            response = {
                "success": True,
                "message": "This client was inserted successfully",
                "code": HTTPStatus.CREATED,
            }

        except ValueError as exception:
            response = {
                "success": False,
                "message": "Invalid parameters",
                "code": HTTPStatus.BAD_REQUEST,
            }

        except ClientAlreadyExists as exception:
            response = {
                "success": False,
                "message": "There is already exists a client with this email",
                "code": HTTPStatus.BAD_REQUEST,
            }

        except Exception as exception:
            response = {
                "success": False,
                "message": "Error to create a client",
                "code": HTTPStatus.INTERNAL_SERVER_ERROR,
            }

        return response

    @staticmethod
    def update_client_by_id(request_body: dict, client_id: int) -> dict:
        try:
            ClientCarfordService.update_client_by_id(
                client_changes=request_body, client_id=client_id
            )
            response = {
                "success": True,
                "message": "This client was updated successfully",
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

        except Exception as exception:
            response = {
                "success": False,
                "message": "Error to update this client",
                "code": HTTPStatus.INTERNAL_SERVER_ERROR,
            }

        return response

    @staticmethod
    def delete_client_by_id(client_id: int) -> dict:
        try:
            ClientCarfordService.delete_client_by_id(client_id=client_id)
            response = {
                "success": True,
                "message": "This client and their cars was delete successfully",
                "code": HTTPStatus.OK,
            }

        except ClientNotExists as exception:
            response = {
                "success": False,
                "message": "There isn't a client with this id",
                "code": HTTPStatus.BAD_REQUEST,
            }

        except Exception as exception:
            response = {
                "success": False,
                "message": "Error to delete this client",
                "code": HTTPStatus.INTERNAL_SERVER_ERROR,
            }

        return response
