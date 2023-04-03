import sqlalchemy as sq
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

metadata = MetaData()
Base = declarative_base()


class Viewed(Base):
    __tablename__ = 'viewed'

    profile_id = sq.Column(sq.Integer, primary_key=True)
    worksheet_id = sq.Column(sq.Integer, unique=True)
