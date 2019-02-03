from flask import Flask, jsonify, request;
from dao.dao_utils import DAOUtils;
from dao.dborm import Cart
import sys;


class CartHandler:

    @staticmethod
    def add_cart():
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




