from sqlalchemy.exc import SQLAlchemyError
from app.model.entity import User
from app.infra.db import Connection


class UserRepository:

    __postgres_connection: Connection

    def __init__(self) -> None:
        self.__postgres_connection = Connection()
