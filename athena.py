# Local
from src.infrastructure.sqlite.infrastructure import SqliteInfrastructure
from src.routes.base.routes import BaseRoute

app = BaseRoute.register_routes()
SqliteInfrastructure.create_tables()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4001)
