from flask import Flask, jsonify, request;
from dao.dao_utils import DAOUtils;


class CartsHandler:

    @staticmethod
    def __methods_to_func(action):
        switcher = {
            'GET': CartsHandler.__get_carts
        }
        func = switcher.get(action)
        return func()

    @staticmethod
    def carts_handler():
        return CartsHandler.__methods_to_func(action=request.method)

    @staticmethod
    def __get_carts():
        db = DAOUtils.get_db()
        input_json = request.get_json()
        carts = DAOUtils.get_cart_dao().get_carts(db, "USER_ID = '{USER_ID}'", USER_ID=input_json['user_id'])
        result = dict()
        item_list = list()
        for cart in carts:
            item_dict = dict()
            item_dict['item_id'] = int(cart.PRODUCT.ITEM_ID)
            item_dict['item_name'] = cart.PRODUCT.ITEM_NM
            item_dict['item_price'] = int(cart.PRODUCT.ITEM_PRICE)
            item_dict['amount'] = int(cart.AMOUNT)
            item_dict['create_time'] = int(cart.PRODUCT.CREATED_TIME)
            item_dict['subtotal'] = int(cart.PRODUCT.ITEM_PRICE * cart.AMOUNT)
            item_list.append(item_dict)

        DAOUtils.close(db)
        result['total'] = len(carts)
        result['item_list'] = item_list

        return Flask(__name__).make_response((jsonify(result), 200))





