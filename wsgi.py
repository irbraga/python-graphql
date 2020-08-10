
import configparser

from flask import Flask
from flask_graphql import GraphQLView
from flask_migrate import Migrate

from sqlalchemy_config import db
from schema import schema
from app_config import Config
from app_cli import database_cli


def create_app():
    """
    Flask factory pattern.
    https://flask.palletsprojects.com/en/1.1.x/patterns/appfactories/
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initializing the Flask-SQLAlchemy extension.
    db.init_app(app)
    # Creating the Flask-Migration integration.
    Migrate(app,db)
    # Adding a GraphQL Schema to the app
    app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True
        )
    )
    
    # Add a Flask command line option to load initial data to database.
    app.cli.add_command(database_cli)

    return app

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        """
        Rolling back the db session if an exception occured and removing the db session
        at the flask app context ending.
        """
        if exception:
            db.session.rollback()
        db.session.remove()