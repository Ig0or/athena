# Standard
from json import dumps

# Third Party
from flask import Blueprint, request, Response

# Local
from src.controllers.carford.car_controller import CarCarfordController
from src.controllers.carford.client_controller import ClientCarfordController


class CarfordRoutes:
    __carford_routes = Blueprint("carford", __name__)

    @staticmethod
    def get_routers() -> Blueprint:
        return CarfordRoutes.__carford_routes

    @staticmethod
    @__carford_routes.route("/client")
    def get_all_clients() -> Response:
        response = ClientCarfordController.get_all_clients()
        response_json = dumps(response)

        return Response(response=response_json, status=response.get("code"))

    @staticmethod
    @__carford_routes.route("/client/<int:client_id>")
    def get_client_by_id(client_id: int) -> Response:
        response = ClientCarfordController.get_client_by_id(client_id=client_id)
        response_json = dumps(response)

        return Response(response=response_json, status=response.get("code"))

    @staticmethod
    @__carford_routes.route("/client", methods=["POST"])
    def create_client() -> Response:
        request_body = request.json

        response = ClientCarfordController.create_client(request_body=request_body)
        response_json = dumps(response)

        return Response(response=response_json, status=response.get("code"))

    @staticmethod
    @__carford_routes.route("/client/<int:client_id>", methods=["PUT"])
    def update_client_by_id(client_id: int) -> Response:
        request_body = request.json

        response = ClientCarfordController.update_client_by_id(
            request_body=request_body, client_id=client_id
        )
        response_json = dumps(response)

        return Response(response=response_json, status=response.get("code"))

    @staticmethod
    @__carford_routes.route("/client/<int:client_id>", methods=["DELETE"])
    def delete_client_by_id(client_id: int) -> Response:
        response = ClientCarfordController.delete_client_by_id(client_id=client_id)
        response_json = dumps(response)

        return Response(response=response_json, status=response.get("code"))

    @staticmethod
    @__carford_routes.route("/car")
    def get_all_cars() -> Response:
        response = CarCarfordController.get_all_cars()
        response_json = dumps(response)

        return Response(response=response_json, status=response.get("code"))

    @staticmethod
    @__carford_routes.route("/car/<int:car_id>")
    def get_car_by_id(car_id: int) -> Response:
        response = CarCarfordController.get_car_by_id(car_id=car_id)
        response_json = dumps(response)

        return Response(response=response_json, status=response.get("code"))

    @staticmethod
    @__carford_routes.route("/car", methods=["POST"])
    def create_car() -> Response:
        request_body = request.json

        response = CarCarfordController.create_car(request_body=request_body)
        response_json = dumps(response)

        return Response(response=response_json, status=response.get("code"))

    @staticmethod
    @__carford_routes.route("/car/<int:car_id>", methods=["DELETE"])
    def delete_car_by_id(car_id: int) -> Response:
        response = CarCarfordController.delete_car_by_id(car_id=car_id)
        response_json = dumps(response)

        return Response(response=response_json, status=response.get("code"))
