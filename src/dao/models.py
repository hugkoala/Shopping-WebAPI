from sqlalchemy import create_engine;
from sqlalchemy.orm import sessionmaker;


# Setting Database Info

host = 'localhost'
port = 1521
sid = 'orcl'
username = 'DEV_WEB_API'
password = '123456'


engine = create_engine(
    'oracle://{0}:{1}@{2}:{3}/{4}'.format(username, password, host, port, sid),
    # convert_unicode=False,
    pool_recycle=10,
    pool_size=50,
    echo=True
)

Database = sessionmaker(bind=engine)
db = Database()


class DAO:

    @staticmethod
    def commit():
        db.commit()

    @staticmethod
    def rollback():
        db.rollback()

    @staticmethod
    def close():
        db.close()

    @staticmethod
    def query_first(obj=None, condition='', **kwargs):
        if not obj:
            return
        if condition == '':
            return db.query(obj).first()
        else:
            return db.query(obj).filter(condition.format(**kwargs)).first()

    @staticmethod
    def query_list(obj=None, condition='', **kwargs):
        if not obj:
            return
        if condition == '':
            return db.query(obj).all()
        else:
            return db.query(obj).filter(condition.format(**kwargs)).all()

    @staticmethod
    def insert(obj):
        db.add(obj)

    @staticmethod
    def update(obj=None, condition='', **kwargs):
        if not obj:
            return

    @staticmethod
    def delete(obj):
        db.delete(obj)



