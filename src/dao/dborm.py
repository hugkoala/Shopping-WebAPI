from sqlalchemy.ext.declarative import declarative_base;
from sqlalchemy import Column, String, Numeric;
import uuid, time;
from hashlib import md5;

Base = declarative_base()


# Setting Table Column

class User(Base):
    __tablename__= 'USERS'

    ACCOUNT = Column('ACCOUNT', String(20))
    PASSWORD = Column('PASSWORD', String(50))
    NAME = Column('NAME', String(20))
    USER_ID = Column('USER_ID', String(10), primary_key=True)
    CREDIT = Column('CREDIT', String(30))
    CREATED_TIME = Column('CREATED_TIME', Numeric(13))
    LAST_LOGIN_TIME = Column('LAST_LOGIN_TIME', Numeric(13))

    def __init__(self, account=None, pwd=None, name=None, credit=None):
        self.ACCOUNT = account
        self.PASSWORD = md5(pwd.encode('utf-8')).hexdigest()
        self.NAME = name
        self.CREDIT = credit
        self.USER_ID = str(uuid.uuid4())
        self.CREATED_TIME = int(round(time.time() * 1000))
        self.LAST_LOGIN_TIME = int(round(time.time() * 1000))
