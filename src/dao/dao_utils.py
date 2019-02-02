from .models import DAO;


class DAOUtils(DAO):

    @staticmethod
    def get_user_dao():
        from .user_dao_impl import UserDAOImpl
        # return user_dao_impl()
        return UserDAOImpl()
