
from flask.cli import AppGroup
from sqlalchemy_config import db
from entities import Room, UserRoomInfo, User

database_cli = AppGroup("database")

@database_cli.command()
def load():
    """
    Load initial data to databse via Flask CLI.
    """

    neo = User()
    neo.name = "Neo"
    neo.email = "neo@thematrix.com"

    trinity = User()
    trinity.name = "Trinity"
    trinity.email = "trinity@thematrix.com"

    morpheus = User()
    morpheus.name = "Morpheus"
    morpheus.email = "morpheus@thematrix.com"

    neo_just_friend_room = UserRoomInfo()
    neo_just_friend_room.user = neo

    trinity_just_friend_room = UserRoomInfo()
    trinity_just_friend_room.user = trinity

    morpheus_just_friend_room = UserRoomInfo()
    morpheus_just_friend_room.user = morpheus

    just_friends = Room()
    just_friends.name = "Just friends against the Matrix!!"
    just_friends.users = [neo_just_friend_room,trinity_just_friend_room,morpheus_just_friend_room]

    db.session.add(just_friends)
    db.session.commit()
