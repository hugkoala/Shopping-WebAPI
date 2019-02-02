from .models import DAO
from .user_dao import UserDAO
from .dborm import User


class UserDAOImpl(UserDAO):
    @staticmethod
    def get_users():
        return DAO.query_list(User)

    @staticmethod
    def get_users(condition, **kwargs):
        return DAO.query_list(User, condition, **kwargs)

    @staticmethod
    def get_user(condition, **kwargs):
        return DAO.query_first(User, condition, **kwargs)

    @staticmethod
    def insert_user(user):
        DAO.insert(user)
        DAO.commit()


