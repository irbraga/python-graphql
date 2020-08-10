
import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy_config import db


class Room(db.Model):
    """
    This entity represents a chatroom.
    """
    __tablename__ = "rooms"

    id = Column(Integer, primary_key = True)
    name = Column(String(50), nullable = False)
    created_on = Column(DateTime, nullable = False, default = datetime.datetime.now())
    
    users = relationship("UserRoomInfo", cascade="all, delete")
    # messages = relationship("Message", uselist = True, backref="room", cascade = "all, delete-orphan")

class User(db.Model):
    """
    This entity represents a chatroom user.
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    name = Column(String(50), nullable = False)
    email = Column(String(50), unique = True, nullable = False)

class UserRoomInfo(db.Model):
    """
    Class to represent a many-to-many mapping between Room and User.
    https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html#association-object
    """

    __tablename__ = "user_room_info"

    id = Column(Integer, primary_key = True)
    added_on = Column(DateTime, nullable = False, default = datetime.datetime.now())

    room_id = Column(Integer, ForeignKey(Room.id))
    user_id = Column(Integer, ForeignKey(User.id))
    user = relationship(User, cascade="all, delete")

# class Message(db.Model):

#     __tablename__ = "messages"
    
#     id = Column(Integer, primary_key = True)
#     message = Column(String, nullable = False)
#     sent_on = Column(DateTime, nullable = False, default = datetime.datetime.now())