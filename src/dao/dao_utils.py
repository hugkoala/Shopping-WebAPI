from user_dao_impl import UserDAOImpl;

class DAOUtils:

    @staticmethod
    def get_user_dao():
        return UserDAOImpl()