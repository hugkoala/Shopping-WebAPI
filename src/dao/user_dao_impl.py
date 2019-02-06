from .dao_utils import DAOUtils;
from .user_dao import UserDAO;
from .dborm import User;


class UserDAOImpl(UserDAO):
    @staticmethod
    def get_users(db):
        return DAOUtils.query_list(db, User)

    @staticmethod
    def get_users(db, condition, **kwargs):
        return DAOUtils.query_list(db, User, condition, **kwargs)

    @staticmethod
    def get_user(db, condition, **kwargs):
        return DAOUtils.query_first(db, User, condition, **kwargs)

    @staticmethod
    def insert_user(db, user):
        try:
            DAOUtils.insert(db, user)
        except:
            raise



