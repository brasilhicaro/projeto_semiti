from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.model import Base
from app.model.enums import GameGender


class Game(Base):

    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    year = Column(Integer)
    platform = Column(String)
    genre = Column(GameGender)
    publisher = Column(String)
    library_id = Column(Integer, ForeignKey("libraries.id"))
    library = relationship("Library", back_populates="games")
