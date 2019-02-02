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
    def close():
        db.close()

    @staticmethod
    def query_first(obj):
        return db.query(obj).one()

    @staticmethod
    def query_list(obj):
        return db.query(obj).all()

    @staticmethod
    def insert(obj):
        db.add(obj)

if __name__ == '__main__':
    from dborm import User
    from dao_utils import DAOUtils
    db = Database()

    user = User(account='leo.li1', pwd='123456', name='Leo', credit='est125')

    # DAOUtils.get_user_dao().insert_user(user)
    users = DAOUtils.get_user_dao().get_users()
    for item in users:
        print(item.ACCOUNT)



