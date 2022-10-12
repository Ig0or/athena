# Local
from src.infrastructure.sqlite.infrastructure import SqliteInfrastructure


class BaseCarfordRepository:
    session = SqliteInfrastructure.get_session()
