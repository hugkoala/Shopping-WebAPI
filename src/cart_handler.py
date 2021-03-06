from flask import Flask, jsonify, request, json;
from src.dao.dao_utils import DAOUtils;
from src.dao.dborm import Cart
from src.log_utils import LogUtils;
import sys;


class CartHandler:

    @staticmethod
    def __methods_to_func(action):
        """
        Request method to function
        :param action:Request method
        :return:function
        """
        switcher = {
            'POST': CartHandler.__add_cart,
            'DELETE': CartHandler.__delete_cart
        }
        func = switcher.get(action)
        return func()

    @staticmethod
    def cart_handler():
        return CartHandler.__methods_to_func(action=request.method)

    @staticmethod
    def __add_cart():
        """
        Add Item to Cart
        :return: Response
        """
        db = DAOUtils.get_db()
        input_json = request.get_json()
        user = DAOUtils.get_user_dao().get_user(db, condition="USER_ID = '{USER_ID}'", USER_ID=input_json['user_id'])
        product = DAOUtils.get_product_dao().get_product(db, "ITEM_ID = '{ITEM_ID}'", ITEM_ID=input_json['item_id'])
        if user and product:
            if input_json['amount'] > product.AMOUNT:
                DAOUtils.close(db)
                error_result = dict()
                error_result['error'] = '商品庫存不足'
                return Flask(__name__).make_response((jsonify(error_result), 403))
            else:
                product.AMOUNT -= input_json['amount']
                cart = Cart(user_id=input_json['user_id'], item_id=input_json['item_id'], amount=input_json['amount'])
                try:
                    DAOUtils.get_cart_dao().insert_cart(db, cart)
                    LogUtils.insert_user_log(db, user_id=input_json['user_id'],
                                             action='加入商品至購物車', remark=str(json.dumps(input_json)))
                    DAOUtils.commit(db)
                    return Flask(__name__).make_response(('', 201))
                except:
                    DAOUtils.rollback(db)
                    error_result = dict()
                    error_result['error'] = str(sys.exc_info())
                    return Flask(__name__).make_response((jsonify(error_result), 406))
                finally:
                    DAOUtils.close(db)
        else:
            DAOUtils.close(db)
            return Flask(__name__).make_response(('', 404))

    @staticmethod
    def __delete_cart():
        """
        Remove Item from Cart
        :return: Response
        """
        db = DAOUtils.get_db()
        input_json = request.get_json()
        user = DAOUtils.get_user_dao().get_user(db, condition="USER_ID = '{USER_ID}'", USER_ID=input_json['user_id'])
        product = DAOUtils.get_product_dao().get_product(db, "ITEM_ID = '{ITEM_ID}'", ITEM_ID=input_json['item_id'])

        if user and product:
            try:
                carts = DAOUtils.get_cart_dao().get_carts(db,
                                                          condition="USER_ID = '{USER_ID}' AND ITEM_ID = '{ITEM_ID}'",
                                                          USER_ID=input_json['user_id'], ITEM_ID=input_json['item_id'])
                if carts:
                    for cart in carts:
                        DAOUtils.get_cart_dao().delete_cart(db, cart)
                        product.AMOUNT += cart.AMOUNT
                    LogUtils.insert_user_log(db, user_id=input_json['user_id'],
                                             action='移除商品至購物車', remark=str(json.dumps(input_json)))
                    DAOUtils.commit(db)
                    return Flask(__name__).make_response(('', 200))
                else:
                    return Flask(__name__).make_response(('', 404))
            except:
                DAOUtils.rollback(db)
                error_result = dict()
                error_result['error'] = str(sys.exc_info())
                return Flask(__name__).make_response((jsonify(error_result), 406))
            finally:
                DAOUtils.close(db)
        else:
            DAOUtils.close(db)
            return Flask(__name__).make_response(('', 404))




