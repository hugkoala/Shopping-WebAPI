from sqlalchemy.ext.declarative import declarative_base;
from sqlalchemy import Column, String, Numeric;
import uuid, time;

Base = declarative_base()


# Setting Table Column

class User(Base):
    __tablename__= 'USERS'

    ACCOUNT = Column('ACCOUNT', String(20))
    PASSWORD = Column('PASSWORD', String(50))
    NAME = Column('NAME', String(20))
    USER_ID = Column('USER_ID', String(10), primary_key=True)
    CREDIT = Column('CREDIT', String(30))
    LAST_LOGIN_TIME = Column('LAST_LOGIN_TIME', Numeric(13))

    def __init__(self, account=None, pwd=None, name=None, credit=None):
        self.ACCOUNT = account
        self.PASSWORD = pwd
        self.NAME = name
        self.CREDIT = credit
        self.USER_ID = str(uuid.uuid4())
        self.LAST_LOGIN_TIME = int(round(time.time() * 1000))
