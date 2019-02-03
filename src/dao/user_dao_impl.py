from .dao_utils import DAOUtils;
from .user_dao import UserDAO;
from .dborm import User;


class UserDAOImpl(UserDAO):
    @staticmethod
    def get_users():
        return DAOUtils.query_list(User)

    @staticmethod
    def get_users(condition, **kwargs):
        return DAOUtils.query_list(User, condition, **kwargs)

    @staticmethod
    def get_user(condition, **kwargs):
        return DAOUtils.query_first(User, condition, **kwargs)

    @staticmethod
    def insert_user(user):
        try:
            DAOUtils.insert(user)
        except:
            raise



