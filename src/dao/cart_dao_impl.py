from .dao_utils import DAOUtils;
from .cart_dao import CartDAO;


class CartDAOImpl(CartDAO):

    @staticmethod
    def insert_cart(cart):
        try:
            DAOUtils.insert(cart)
        except:
            raise



