
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from entities import Room as RoomEntity, User as UserEntity, UserRoomInfo as UserRoomInfoEntity

class User(SQLAlchemyObjectType):
    """
    Class mapping to map the database entity User to a GraphQL object.
    """
    class Meta:
        model = UserEntity
        interfaces = (relay.Node, )

class UserRoomInfo(SQLAlchemyObjectType):

    class Meta:
        model = UserRoomInfoEntity
        interfaces = (relay.Node, )

class Room(SQLAlchemyObjectType):
    """
    Class mapping to map the database entity Room to a GraphQL object.
    """
    class Meta:
        model = RoomEntity
        interfaces = (relay.Node, )

    users = graphene.List(UserRoomInfo)

class Query(graphene.ObjectType):
    """
    Query object to perform the information lookup.
    """
    node = relay.Node.Field()
    all_rooms = SQLAlchemyConnectionField(Room.connection)
    all_users = SQLAlchemyConnectionField(User.connection, sort=None)

# GraphQL Shema definition
schema = graphene.Schema(query=Query)