from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.model import Base


class Library(Base):

    __tablename__ = "libraries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    user = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="library")
    games_id = Column(Integer, ForeignKey("games.id"))
    games = relationship("Game", back_populates="library")
