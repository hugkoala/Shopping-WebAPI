from .dao_utils import DAOUtils;
from .cart_dao import CartDAO;
from .dborm import Cart;


class CartDAOImpl(CartDAO):

    @staticmethod
    def insert_cart(cart):
        try:
            DAOUtils.insert(cart)
        except:
            raise

    @staticmethod
    def get_carts(condition, **kwargs):
        return DAOUtils.query_list(Cart, condition, **kwargs)

    @staticmethod
    def delete_cart(cart):
        DAOUtils.delete(cart)



