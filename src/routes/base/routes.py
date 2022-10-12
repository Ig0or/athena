# Standard
from json import dumps

# Third Party
from flask import Flask, Response

# Local
from src.routes.carford.routes import CarfordRoutes


class BaseRoute:
    app = Flask("Athena")

    @staticmethod
    @app.route("/")
    def health_check() -> Response:
        response = {"success": True, "message": "Athena is alive."}
        response_json = dumps(response)

        return Response(response=response_json)

    @classmethod
    def __register_carford_routes(cls) -> Flask:
        carford_routers = CarfordRoutes.get_routers()
        BaseRoute.app.register_blueprint(carford_routers)

        return cls.app

    @classmethod
    def register_routes(cls) -> Flask:
        cls.__register_carford_routes()

        return cls.app
