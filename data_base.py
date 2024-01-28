from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://yumi:postgres@172.19.0.2:5432/online_shop')
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
db_engine = create_engine('postgresql://yumi:postgres@172.19.0.2:5432/online_shop')
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    import models
    Base.metadata.create_all(bind=engine)
    Base.query = db_session.query_property()