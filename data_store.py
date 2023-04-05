import sqlalchemy
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base

from sqlalchemy.orm import sessionmaker

DSN = 'postgresql://postgres:230796@localhost:5432/data_store'
engine = sqlalchemy.create_engine(DSN)

if __name__ == 'main':
    from sqlalchemy import create_engine, MetaData
    create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()
metadata = MetaData()
Base = declarative_base()


session.commit()


def create_tables(profile_id, worksheet_id):
    profile_id = profile_id
    worksheet_id = worksheet_id

    profile_id = sq.Column(sq.Integer, primary_key=True)
    worksheet_id = sq.Column(sq.Integer, unique=True)


class Viewed(Base):
    __tablename__ = 'viewed'

    def __str__(self):
        return f'Viewed {self.id}:({self.profile_id}, {self.worksheet_id})'


def create_table(self):
    Base.metadata.drop_all(self)
    Base.metadata.create_all(self)


session.commit()
