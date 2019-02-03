from sqlalchemy.ext.declarative import declarative_base;
from sqlalchemy import Column, String, Numeric, ForeignKey;
import uuid, time;
from hashlib import md5;
from sqlalchemy.orm import relationship;

Base = declarative_base()


# Setting Table Column

class User(Base):
    __tablename__= 'USERS'

    ACCOUNT = Column('ACCOUNT', String(20))
    PASSWORD = Column('PASSWORD', String(50))
    NAME = Column('NAME', String(20))
    USER_ID = Column('USER_ID', String(36), primary_key=True)
    CREDIT = Column('CREDIT', String(30))
    CREATED_TIME = Column('CREATED_TIME', Numeric(13))
    LAST_LOGIN_TIME = Column('LAST_LOGIN_TIME', Numeric(13))

    CART = relationship('Cart')

    def __init__(self, account=None, pwd=None, name=None, credit=None):
        self.ACCOUNT = account
        self.PASSWORD = md5(pwd.encode('utf-8')).hexdigest()
        self.NAME = name
        self.CREDIT = credit
        self.USER_ID = str(uuid.uuid4())
        self.CREATED_TIME = int(round(time.time() * 1000))
        self.LAST_LOGIN_TIME = int(round(time.time() * 1000))


class Product(Base):
    __tablename__ = 'PRODUCTS'

    ITEM_ID = Column('ITEM_ID', Numeric(10), primary_key=True)
    ITEM_NM = Column('ITEM_NM', String(30))
    ITEM_PRICE = Column('ITEM_PRICE', Numeric(10))
    AMOUNT = Column('AMOUNT', Numeric(8))
    CREATED_TIME = Column('CREATED_TIME', Numeric(13))

    def __init__(self, item_id=0, item_nm=None, item_price=0, amount=0):
        self.ITEM_ID = item_id
        self.ITEM_NM = item_nm
        self.ITEM_PRICE = item_price
        self.AMOUNT = amount
        self.CREATED_TIME = int(round(time.time() * 1000))


class Cart(Base):
    __tablename__ = 'CART'

    CART_ID = Column('CART_ID', String(36), primary_key=True)
    USER_ID = Column('USER_ID', String(36), ForeignKey('USERS.USER_ID'))
    ITEM_ID = Column('ITEM_ID', Numeric(10), ForeignKey('PRODUCTS.ITEM_ID'))
    AMOUNT = Column('AMOUNT', Numeric(8))

    def __init__(self, user_id=None, item_id=None, amount=None):
        self.CART_ID = str(uuid.uuid4())
        self.USER_ID = user_id
        self.ITEM_ID = item_id
        self.AMOUNT = amount


