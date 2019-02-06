from .dao_utils import DAOUtils;
from .cart_dao import CartDAO;
from .dborm import Cart;


class CartDAOImpl(CartDAO):

    @staticmethod
    def insert_cart(db, cart):
        try:
            DAOUtils.insert(db, cart)
        except:
            raise

    @staticmethod
    def get_carts(db, condition, **kwargs):
        return DAOUtils.query_list(db, Cart, condition, **kwargs)

    @staticmethod
    def delete_cart(db, cart):
        DAOUtils.delete(db, cart)



