from sqlalchemy import create_engine;
from sqlalchemy.orm import sessionmaker;
from sqlalchemy.sql import elements;
from sqlalchemy.ext.declarative.api import DeclarativeMeta;


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
        if not (isinstance(obj, elements.Label) or isinstance(obj, DeclarativeMeta)):
            return
        return DAO.__query_filter(
            obj=obj,
            condition=condition,
            query_type='one',
            **kwargs
        )

    @staticmethod
    def query_list(obj=None, condition='', **kwargs):
        if not (isinstance(obj, elements.Label) or isinstance(obj, DeclarativeMeta)):
            return
        if condition == '':
            return db.query(obj).all()
        else:
            return db.query(obj).filter(condition.format(**kwargs)).all()

    @staticmethod
    def __query_filter(obj=None, condition='', query_type=None, **kwargs):
        if condition == '':
            return DAO.__query_type(
                obj=obj,
                query_type=query_type,
                query_filter=None
            )
        elif isinstance(condition, str):
            return DAO.__query_type(
                obj=obj,
                query_type=query_type,
                query_filter=condition.format(**kwargs)
            )
        elif isinstance(condition, elements.BooleanClauseList) or isinstance(condition, elements.BinaryExpression):
            return DAO.__query_type(
                obj=obj,
                query_type=query_type,
                query_filter=condition
            )

    @staticmethod
    def __query_type(obj=None, query_type=None, query_filter=None):
            if query_type == 'one':
                return db.query(obj).filter(query_filter).first()
            else:
                return db.query(obj).filter(query_filter).all()

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



