import sqlalchemy as sq
import psycopg2
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session

from config import db_url

metadata = MetaData()
Base = declarative_base()


class Viewed(Base):
    __tablename__ = 'viewed'
    profile_id = sq.Column(sq.Integer, primary_key=True)
    worksheet_id = sq.Column(sq.Integer, primary_key=True)

    def add_user(profile_id, worksheet_id):
        engine = create_engine(db_url)
        Base.metadata.create_all(engine)
        with Session(engine) as session:
            to_bd = Viewed(profile_id=profile_id, worksheet_id=worksheet_id)
            connection = psycopg2.connect(db_url)
            cursor = connection.cursor()

            record_to_insert = ()
            cursor.execute(record_to_insert)

            connection.commit()

            session.add(to_bd)
            session.commit()

    def check_user(profile_id, worksheet_id):
        engine = create_engine(db_url)
        Base.metadata.create_all(engine)
        with Session(engine) as session:
            from_bd = session.query(Viewed).filter(
                Viewed.profile_id == profile_id,
                Viewed.worksheet_id == worksheet_id
            ).first()
            return True if from_bd else False

    def user_search(self, user, photos_user, user_id):
        connection = psycopg2.connect(db_url)
        cursor = connection.cursor()

        record_to_insert = ()
        cursor.execute(record_to_insert)

        connection.commit()

        photos_attachment = ",".join(photos_user)
        user_answer = []
        profile_id = []
        worksheet_id = []
        to_bd = Viewed(profile_id=profile_id, worksheet_id=worksheet_id)

        session = db_url.Session()
        if user_answer == '1':
            dating_user = db_url.DatingUser(['id'], user['first_name'],
                                            user['last_name'], user['bdate'],
                                            user['sex'], user['city'], photos_attachment,
                                            user_id)
            session.add(dating_user)
        elif user_answer == '2':
            black_list_item = db_url.BlackList(user['id'], user['first_name'],
                                               user['last_name'], user['bdate'],
                                               user['sex'], user['city'],
                                               photos_attachment, user_id)
            session.add(black_list_item)
        elif user_answer == '3':
            self.worksheets()
            return False

        session.add(to_bd)
        session.commit()
