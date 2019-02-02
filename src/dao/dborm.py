from sqlalchemy.ext.declarative import declarative_base;
from sqlalchemy import Column, String;
import uuid;

Base = declarative_base()


# Setting Table Column

class User(Base):
    __tablename__= 'USERS'

    ACCOUNT = Column('ACCOUNT', String(20))
    PASSWORD = Column('PASSWORD', String(50))
    NAME = Column('NAME', String(20))
    USER_ID = Column('USER_ID', String(10), primary_key=True)
    CREDIT = Column('CREDIT', String(30))

    def __init__(self, account=None, pwd=None, name=None, credit=None):
        self.ACCOUNT = account
        self.PASSWORD = pwd
        self.NAME = name
        self.CREDIT = credit
        self.USER_ID = str(uuid.uuid4())
