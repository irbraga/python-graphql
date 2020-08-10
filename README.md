# python-graphql

A projetc using Graphene framework and SQLAlchemy.

## Project's purpose

This projects aims to create a live chat using [PostgreSQL's pubsub](https://www.postgresql.org/docs/12/sql-notify.html) feature and GraphQL subscriptions.

## Project requirements

* [Python 3](https://www.python.org/downloads/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [Graphene](https://graphene-python.org/)

This project uses some extensions to help integrate these frameworks and add functionalities to improve development:

* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
* [Flask-GraphQL](https://github.com/graphql-python/flask-graphql)
* [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)
* [graphene_sqlalchemy](https://github.com/graphql-python/graphene-sqlalchemy)

Also, a [PostgreSQL](https://www.postgresql.org/) database is used and a driver to connect the database is required:

* [psycopg2-binary](https://www.psycopg.org/)