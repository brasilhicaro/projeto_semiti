from app.model.entity import Library
from app.infra.db import Connection
from sqlalchemy.exc import SQLAlchemyError


class LibraryRepository:
    __postgres_connection: Connection

    def __init__(self) -> None:
        """
        _summary_: Method responsible for initializing the class
        """
        self.__postgres_connection = Connection()

    def create(self, library: Library):
        try:
            self.__postgres_connection.__session.add(library)
            self.__postgres_connection.__session.flush()
            self.__postgres_connection.__session.commit()
            return library
        except SQLAlchemyError as e:
            self.__postgres_connection.__session.rollback()
            raise e

    def get_all(self):
        try:
            return self.__postgres_connection.__session.query(Library).all()
        except SQLAlchemyError as e:
            self.__postgres_connection.__session.rollback()
            raise e

    def get_by_id(self, library_id: int):
        if library_id is None:
            raise ValueError("library_id is required")
        try:
            return (
                self.__postgres_connection.__session.query(Library)
                .filter(Library.id == library_id)
                .first()
            )
        except SQLAlchemyError as e:
            self.__postgres_connection.__session.rollback()
        raise e

    def update(self, library: Library):
        try:
            self.__postgres_connection.__session.merge(library)
            self.__postgres_connection.__session.flush()
            self.__postgres_connection.__session.commit()
            return library
        except SQLAlchemyError as e:
            self.__postgres_connection.__session.rollback()
            raise e
