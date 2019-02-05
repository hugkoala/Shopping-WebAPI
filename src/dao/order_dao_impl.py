from .dao_utils import DAOUtils;
from .order_dao import OrderDAO;
from .dborm import OrderHeader, OrderItem;
import datetime;


class OrderDAOImpl(OrderDAO):

    @staticmethod
    def insert_order_header(order_header):
        try:
            DAOUtils.insert(order_header)
        except:
            raise

    @staticmethod
    def insert_order_item(order_item):
        try:
            DAOUtils.insert(order_item)
        except:
            raise

    @staticmethod
    def get_max_order_no():
        from sqlalchemy import func
        today_str = datetime.datetime.now().strftime('%Y%m%d')
        condition_str = 'AP' + today_str + '%'
        max_ord_no = DAOUtils.query_first(obj=func.max(OrderHeader.ORD_NO).label('MAX_ORD_NO'),
                                          condition=OrderHeader.ORD_NO.like(condition_str))
        if max_ord_no[0]:
            return 'AP' + today_str + str(int(max_ord_no[0][10:]) + 1).rjust(5, '0')
        else:
            return 'AP' + today_str + '00001'




