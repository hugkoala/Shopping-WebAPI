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
    CREDIT = Column('CREDIT', Numeric(20))
    CREATED_TIME = Column('CREATED_TIME', Numeric(13))
    LAST_LOGIN_TIME = Column('LAST_LOGIN_TIME', Numeric(13))

    USER_LOGS = relationship('UserLog')

    def __init__(self, account=None, pwd=None, name=None, credit=None):
        self.ACCOUNT = account
        self.PASSWORD = md5(pwd.encode('utf-8')).hexdigest()
        self.NAME = name
        self.CREDIT = credit
        self.USER_ID = str(uuid.uuid4())
        self.CREATED_TIME = int(round(time.time() * 1000))
        self.LAST_LOGIN_TIME = int(round(time.time() * 1000))


class UserLog(Base):
    __tablename__ = 'USERS_LOG'

    USER_LOG_ID = Column('USER_LOG_ID', String(36), primary_key=True)
    USER_ID = Column('USER_ID', String(36), ForeignKey('USERS.USER_ID'))
    ACTION = Column('ACTION', String(30))
    CREATED_TIME = Column('CREATED_TIME', Numeric(13))
    REMARK = Column('REMARK', String(200))

    def __init__(self, user_id=None, action=None, remark=None):
        self.USER_LOG_ID = str(uuid.uuid4())
        self.USER_ID = user_id
        self.ACTION = action
        self.CREATED_TIME = int(round(time.time() * 1000))
        self.REMARK = remark


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

    PRODUCT = relationship('Product')
    USER = relationship('User')

    def __init__(self, user_id=None, item_id=None, amount=None):
        self.CART_ID = str(uuid.uuid4())
        self.USER_ID = user_id
        self.ITEM_ID = item_id
        self.AMOUNT = amount


class OrderHeader(Base):
    __tablename__ = 'ORDER_HEADER'

    ORD_NO = Column('ORD_NO', String(15), primary_key=True)
    USER_ID = Column('USER_ID', String(36), ForeignKey('USERS.USER_ID'))
    CREATED_TIME = Column('CREATED_TIME', Numeric(13))
    SUB_TOTAL = Column('SUB_TOTAL', Numeric(20))

    USER = relationship('User')
    ORDERITEM = relationship('OrderItem')

    def __init__(self, ord_no=None, user_id=None, sub_total=None):
        self.ORD_NO = ord_no
        self.USER_ID = user_id
        self.CREATED_TIME = int(round(time.time() * 1000))
        self.SUB_TOTAL = sub_total


class OrderItem(Base):
    __tablename__ = 'ORDER_ITEM'

    ORDER_ITEM_ID = Column('ORDER_ITEM_ID', String(36), primary_key=True)
    ORD_NO = Column('ORD_NO', String(15), ForeignKey('ORDER_HEADER.ORD_NO'))
    ITEM_ID = Column('ITEM_ID', Numeric(10), ForeignKey('PRODUCTS.ITEM_ID'))
    AMOUNT = Column('AMOUNT', Numeric(8))

    PRODUCT = relationship('Product')

    def __init__(self, ord_no=None, item_id=None, amount=None):
        self.ORDER_ITEM_ID = str(uuid.uuid4())
        self.ORD_NO = ord_no
        self.ITEM_ID = item_id
        self.AMOUNT = amount

