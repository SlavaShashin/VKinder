import sqlalchemy
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

DSN = 'db_url_object'
engine = sqlalchemy.create_engine(DSN)

if __name__ == 'main':
    from sqlalchemy import create_engine, MetaData

    create_engine(DSN)

engine = create_engine(DSN)
Session = sessionmaker(bind=engine)
session = Session()
metadata = MetaData()
Base = declarative_base()


def create_table(self):
    Base.metadata.drop_all(self)
    Base.metadata.create_all(self)


session.commit()


class Viewed(Base):
    __tablename__ = 'viewed'

    profile_id = sq.Column(sq.Integer, primary_key=True)
    worksheet_id = sq.Column(sq.Integer, unique=True)

    def __str__(self):
        return f'Viewed {self.id}:({self.profile_id}, {self.worksheet_id})'

    def add_db(self, profile_id, worksheet_id):
        to_bd = Viewed(profile_id, worksheet_id)
        session.add(to_bd)

    def extract_db(self):
        from_bd = session.query(Viewed).filter(Viewed.profile_id == 123).all()
        session.commit(from_bd)


session.commit()
