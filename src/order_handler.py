from flask import Flask, jsonify, request, json;
from dao.dao_utils import DAOUtils;
from dao.dborm import OrderHeader, OrderItem, Cart;
from log_utils import LogUtils;
from threading import Lock;
import sys;

lock = Lock()


class OrderHandler:

    @staticmethod
    def cart_to_order():
        input_json = request.get_json()

        with lock:
            carts = DAOUtils.get_cart_dao().get_carts("USER_ID = '{USER_ID}'", USER_ID=input_json['user_id'])

            if carts:
                try:
                    ord_no = DAOUtils.get_order_dao().get_max_order_no()
                    order_header = OrderHeader(ord_no=ord_no, user_id=input_json['user_id'], sub_total=0)
                    DAOUtils.get_order_dao().insert_order_header(order_header)
                    sub_total = 0

                    for cart in carts:
                        sub_total += cart.AMOUNT * cart.PRODUCT.ITEM_PRICE
                        order_item = OrderItem(ord_no=ord_no, item_id=cart.ITEM_ID, amount=cart.AMOUNT)
                        DAOUtils.get_order_dao().insert_order_item(order_item)
                        DAOUtils.get_cart_dao().delete_cart(cart)

                    user = DAOUtils.get_user_dao().get_user("USER_ID = '{USER_ID}'", USER_ID=input_json['user_id'])
                    # 額度不足以結帳
                    if sub_total > user.CREDIT:
                        error_result = dict()
                        error_result['error'] = '額度不足以結帳'
                        return Flask(__name__).make_response((jsonify(error_result), 403))
                    else:
                        order_header.SUB_TOTAL = sub_total
                        user.CREDIT -= sub_total
                        LogUtils.insert_user_log(user_id=input_json['user_id'],
                                                 action='購物車結帳', remark=ord_no)
                        DAOUtils.commit()
                        return Flask(__name__).make_response(('', 204))
                except:
                    DAOUtils.rollback()
                    error_result = dict()
                    error_result['error'] = str(sys.exc_info())
                    return Flask(__name__).make_response((jsonify(error_result), 406))
            else:
                return Flask(__name__).make_response(('', 404))



