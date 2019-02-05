from .models import DAO;


class DAOUtils(DAO):

    @staticmethod
    def get_user_dao():
        from .user_dao_impl import UserDAOImpl
        return UserDAOImpl()

    @staticmethod
    def get_user_log_dao():
        from .user_log_dao_impl import UserLogDAOImpl
        return UserLogDAOImpl()

    @staticmethod
    def get_cart_dao():
        from .cart_dao_impl import CartDAOImpl
        return CartDAOImpl()

    @staticmethod
    def get_order_dao():
        from .order_dao_impl import OrderDAOImpl
        return OrderDAOImpl()
