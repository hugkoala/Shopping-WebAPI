from .dao_utils import DAOUtils;
from .product_dao import ProductDAO;
from .dborm import Product;


class ProductDAOImpl(ProductDAO):

    @staticmethod
    def get_product(condition, **kwargs):
        return DAOUtils.query_first(Product, condition, **kwargs)



