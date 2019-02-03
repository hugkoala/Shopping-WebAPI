from flask import Flask, jsonify, request;
from dao.dao_utils import DAOUtils;
from dao.dborm import Cart
import sys;


class CartHandler:

    @staticmethod
    def __methods_to_func(action):
        switcher = {
            'GET': CartHandler.__get_carts,
            'POST': CartHandler.__add_cart,
            'DELETE': CartHandler.__delete_cart
        }
        func = switcher.get(action)
        return func()

    @staticmethod
    def cart_handler():
        return CartHandler.__methods_to_func(action=request.method)

    @staticmethod
    def __get_carts():
        input_json = request.get_json()
        carts = DAOUtils.get_cart_dao().get_cart("USER_ID = '{USER_ID}'", USER_ID=input_json['user_id'])
        result = dict()
        item_list = list()
        for cart in carts:
            item_dict = dict()
            item_dict['item_id'] = int(cart.PRODUCT.ITEM_ID)
            item_dict['item_name'] = cart.PRODUCT.ITEM_NM
            item_dict['item_price'] = int(cart.PRODUCT.ITEM_PRICE)
            item_dict['amount'] = int(cart.PRODUCT.AMOUNT)
            item_dict['create_time'] = int(cart.PRODUCT.CREATED_TIME)
            item_dict['subtotal'] = int(cart.PRODUCT.ITEM_PRICE * cart.PRODUCT.AMOUNT)
            item_list.append(item_dict)

        result['total'] = len(carts)
        result['item_list'] = item_list

        return Flask(__name__).make_response((jsonify(result), 200))

    @staticmethod
    def __add_cart():
        input_json = request.get_json()
        cart = Cart(user_id=input_json['user_id'], item_id=input_json['item_id'], amount=input_json['amount'])
        try:
            DAOUtils.get_cart_dao().insert_cart(cart)
            DAOUtils.commit()
            return Flask(__name__).make_response(('', 201))
        except:
            DAOUtils.rollback()
            error_result = dict()
            error_result['error'] = str(sys.exc_info())
            return Flask(__name__).make_response((jsonify(error_result), 406))

    @staticmethod
    def __delete_cart():
        input_json = request.get_json()
        cart = DAOUtils.get_cart_dao().get_cart("USER_ID = '{USER_ID}' AND ITEM_ID = '{ITEM_ID}'",
                                                USER_ID=input_json['user_id'], ITEM_ID=input_json['item_id'])

        try:
            DAOUtils.get_cart_dao().delete_cart(cart)
            DAOUtils.commit()
            return Flask(__name__).make_response(('', 204))
        except:
            DAOUtils.rollback()
            error_result = dict()
            error_result['error'] = str(sys.exc_info())
            return Flask(__name__).make_response((jsonify(error_result), 406))




