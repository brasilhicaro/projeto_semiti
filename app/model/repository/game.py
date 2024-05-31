from sqlalchemy.exc import SQLAlchemyError
from app.infra.db import Connection
from app.model.entity import Game


class GameRepository:

    __postgres_connection: Connection

    def __init__(self) -> None:
        """
        _summary_: Method responsible for initializing the class
        """
        self.__postgres_connection = Connection()

    def create(self, game: Game):

        try:
            self.__postgres_connection.__session.add(game)
            self.__postgres_connection.__session.flush()
            self.__postgres_connection.__session.commit()
            return game
        except SQLAlchemyError as e:
            self.__postgres_connection.__session.rollback()
            raise e

    def get_all(self):
        try:
            return self.__postgres_connection.__session.query(Game).all()
        except SQLAlchemyError as e:
            self.__postgres_connection.__session.rollback()
            raise e

    def get_by_id(self, game_id: int):
        if game_id is None:
            raise ValueError("game_id is required")
        try:
            return (
                self.__postgres_connection.__session.query(Game)
                .filter(Game.id == game_id)
                .first()
            )
        except SQLAlchemyError as e:
            self.__postgres_connection.__session.rollback()
            raise e

    def update(self, game: Game):
        try:
            self.__postgres_connection.__session.merge(game)
            self.__postgres_connection.__session.flush()
            self.__postgres_connection.__session.commit()
            return game
        except SQLAlchemyError as e:
            self.__postgres_connection.__session.rollback()
            raise e

    def delete(self, game: Game):
        try:
            self.__postgres_connection.__session.delete(game)
            self.__postgres_connection.__session.flush()
            self.__postgres_connection.__session.commit()
            return game
        except SQLAlchemyError as e:
            self.__postgres_connection.__session.rollback()
            raise e
