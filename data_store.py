import sqlalchemy
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=create_engine)
session = Session()
metadata = MetaData()
Base = declarative_base()

DSN = 'postgresql://postgres:230796@localhost:5432/db_store'
engine = sqlalchemy.create_engine(DSN)


def create_tables(profile_id, worksheet_id):
    profile_id = profile_id
    worksheet_id = worksheet_id


session.commit()


class Viewed(Base):
    __tablename__ = 'viewed'

    profile_id = sq.Column(sq.Integer, primary_key=True)
    worksheet_id = sq.Column(sq.Integer, unique=True)

    def __str__(self):
        return f'Viewed {self.id}:({self.profile_id}, {self.worksheet_id})'


def create_table(create_engine):
    Base.metadata.drop_all(create_engine)
    Base.metadata.create_all(create_engine)


session.commit()
