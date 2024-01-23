from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from app import app

engine = create_engine('postgresql://yumi:postgres@localhost/online_shop')
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
db_engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    import models
    Base.metadata.create_all(bind=engine)
