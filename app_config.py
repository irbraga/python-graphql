
class Config:
    """
    Flask and Flask-SQLAlchemy configuration file.
    """
    DEBUG=True
    PRESERVE_CONTEXT_ON_EXCEPTION=False
    JSONIFY_PRETTYPRINT_REGULAR=True
    SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://postgres:postgres@localhost:5432/pubsub"
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_ECHO=False