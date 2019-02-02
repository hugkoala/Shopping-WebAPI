from models import DAO
from user_dao import UserDAO
from dborm import User


class UserDAOImpl(UserDAO):

    @staticmethod
    def insert_user(user):
        DAO.insert(user)
        DAO.commit()

    @staticmethod
    def get_users():
        return DAO.query_list(User)
