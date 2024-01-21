
from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from alembic import context


db = SQLAlchemy()


def run_migrations_online():
    context.configure(
        url=current_app.config['SQLALCHEMY_DATABASE_URI'],
        target_metadata=db.metadata,
        compare_type=True,
        compare_server_default=True,
        compare_server_default_strict=True,
    )


run_migrations_online()
