# Standard
from typing import NoReturn

# Third Party
from decouple import config
from sqlalchemy import (
    Boolean,
    Column,
    create_engine,
    Integer,
    MetaData,
    String,
    Table,
)
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session


class SqliteInfrastructure:
    __engine = None
    __session = None

    @classmethod
    def __get_engine(cls) -> Engine:
        if cls.__engine is None:
            database_url = config("DATABASE_URL")
            cls.__engine = create_engine(url=database_url)

        return cls.__engine

    @classmethod
    def get_session(cls) -> Session:
        engine = cls.__get_engine()

        if cls.__session is None:
            cls.__session = Session(bind=engine)

        return cls.__session

    @classmethod
    def create_tables(cls) -> NoReturn:
        metadata = MetaData()
        engine = cls.__get_engine()

        Table(
            "CLIENT",
            metadata,
            Column("ID", Integer, autoincrement=True, primary_key=True, nullable=False),
            Column("EMAIL", String(30), nullable=False),
            Column("SALE_OPPORTUNITY", Boolean, nullable=False),
        )

        Table(
            "CAR",
            metadata,
            Column("ID", Integer, autoincrement=True, primary_key=True, nullable=False),
            Column("COLOR", String(15), nullable=False),
            Column("MODEL", String(15), nullable=False),
            Column("CLIENT_ID", Integer, nullable=False),
        )

        metadata.create_all(bind=engine)
