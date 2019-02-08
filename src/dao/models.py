from sqlalchemy import create_engine;
from sqlalchemy.orm import sessionmaker;
from sqlalchemy.sql import elements;
from sqlalchemy.ext.declarative.api import DeclarativeMeta;
import configparser;
import os;

# Setting Database Info

config = configparser.ConfigParser()
config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'db.ini'))

host = config['DEFAULT']['host']
port = config['DEFAULT']['port']
sid = config['DEFAULT']['sid']
username = config['DEFAULT']['username']
password = config['DEFAULT']['password']


engine = create_engine(
    'oracle://{0}:{1}@{2}:{3}/{4}'.format(username, password, host, port, sid),
    # convert_unicode=False,
    # pool_recycle=10,
    # pool_size=50,
    echo=True
)


class DAO:

    @staticmethod
    def get_db():
        """
        Get DB Session
        :return database():
        """
        database = sessionmaker(bind=engine)
        return database()

    @staticmethod
    def commit(db):
        """
        Session Commit

        :param db: database()
        """
        db.commit()

    @staticmethod
    def rollback(db):
        """
        Session Rollback

        :param db: database()
        """
        db.rollback()

    @staticmethod
    def close(db):
        """
        Session Close

        :param db: database()
        """
        db.close()

    @staticmethod
    def query_first(db=None, obj=None, condition='', **kwargs):
        """
        Query first row By ORM Obj & filter condition

        :param db: database()
        :param obj:ORM Object
        :param condition:Filter Condition
        :param kwargs:The value of Filter Condition
        :return DAO.__query_filter()
        """
        if not (isinstance(obj, elements.Label) or isinstance(obj, DeclarativeMeta)):
            return
        return DAO.__query_filter(
            db=db,
            obj=obj,
            condition=condition,
            query_type='one',
            **kwargs
        )

    @staticmethod
    def query_list(db=None, obj=None, condition='', **kwargs):
        """
        Query list By ORM Obj & filter condition

        :param db: database()
        :param obj:ORM Object
        :param condition:Filter Condition
        :param kwargs:The value of Filter Condition
        :return DAO.__query_filter()
        """
        if not (isinstance(obj, elements.Label) or isinstance(obj, DeclarativeMeta)):
            return
        return DAO.__query_filter(
            db=db,
            obj=obj,
            condition=condition,
            query_type='all',
            **kwargs
        )

    @staticmethod
    def __query_filter(db=None, obj=None, condition='', query_type=None, **kwargs):
        """
        Handle condition & kwargs

        :param db: database()
        :param obj:ORM Object
        :param condition:Filter Condition
        :param kwargs:The value of Filter Condition
        :return DAO.__query_type()
        """
        if condition == '':
            return DAO.__query_type(
                db=db,
                obj=obj,
                query_type=query_type,
                query_filter=None
            )
        elif isinstance(condition, str):
            return DAO.__query_type(
                db=db,
                obj=obj,
                query_type=query_type,
                query_filter=condition.format(**kwargs)
            )
        elif isinstance(condition, elements.BooleanClauseList) or isinstance(condition, elements.BinaryExpression):
            return DAO.__query_type(
                db=db,
                obj=obj,
                query_type=query_type,
                query_filter=condition
            )

    @staticmethod
    def __query_type(db=None, obj=None, query_type=None, query_filter=None):
        """
        Query By Filter & ORM Object

        :param db: database()
        :param obj:ORM Object
        :param query_type:one or all
        :param query_filter:Handled Filter
        :return obj or the list of obj
        """
        if query_type == 'one':
            return db.query(obj).filter(query_filter).first()
        else:
            return db.query(obj).filter(query_filter).all()

    @staticmethod
    def insert(db, obj):
        """
        Session Insert

        :param db: database()
        :param obj: ORM Object instance
        """
        db.add(obj)

    @staticmethod
    def delete(db, obj):
        """
        Session Delete

        :param db: database()
        :param obj: ORM Object instance
        """
        db.delete(obj)



