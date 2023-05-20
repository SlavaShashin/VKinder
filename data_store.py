import sqlalchemy
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError, InvalidRequestError

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


class User(Base):
    __tablename__ = 'user'
    id = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
    vk_id = sq.Column(sq.Integer, unique=True)


class Photos(Base):
    __tablename__ = 'photos'
    id = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
    link_photo = sq.Column(sq.String)
    count_likes = sq.Column(sq.Integer)
    id_dating_user = sq.Column(sq.Integer, sq.ForeignKey('dating_user.id', ondelete='CASCADE'))


class SelectedProfiles(Base):
    __tablename__ = 'selected_profiles'
    id = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
    vk_id = sq.Column(sq.Integer, unique=True)
    first_name = sq.Column(sq.String)
    second_name = sq.Column(sq.String)
    city = sq.Column(sq.String)
    link = sq.Column(sq.String)
    id_user = sq.Column(sq.Integer, sq.ForeignKey('user.id', ondelete='CASCADE'))


class Viewed(Base):
    __tablename__ = 'viewed'

    profile_id = sq.Column(sq.Integer, primary_key=True)
    worksheet_id = sq.Column(sq.Integer, unique=True)

    def __str__(self):
        return f'Viewed {self.id}:({self.profile_id}, {self.worksheet_id})'

    def add_db(self, profile_id, worksheet_id):
        to_bd = Viewed(profile_id, worksheet_id)
        session.add(to_bd)
        return to_bd

    def extract_db(self):
        from_db = session.query(Viewed).filter(Viewed.profile_id == 123).all()
        session.commit(self)
        return from_db


class Functions(Base):
    def check_db(self):
        current_user_id = session.query(User).filter_by(vk_id=self).first()
        return current_user_id

    def check_db_user(self):
        dating_user = session.query(SelectedProfiles).filter_by(
            vk_id=self).first()
        blocked_user = session.query(SelectedProfiles).filter_by(
            vk_id=self).first()
        return dating_user, blocked_user

    def register_user(self):
        try:
            new_user = User(vk_id=self)
            session.add(new_user)
            session.commit()
            return True
        except (IntegrityError, InvalidRequestError):
            return False


session.commit()
