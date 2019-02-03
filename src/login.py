from flask import Flask, request, jsonify, json;
from dao.dao_utils import DAOUtils;
import time;
from hashlib import md5;


class Login:

    @staticmethod
    def login():
        input_json = request.get_json()
        user = DAOUtils.get_user_dao().get_user(condition="ACCOUNT = '{ACCOUNT}' AND PASSWORD = '{PASSWORD}'",
                                                ACCOUNT=input_json['account'],
                                                PASSWORD=md5(input_json['password'].encode('utf-8')).hexdigest())

        if user:
            result = dict()
            result['user_id'] = user.USER_ID
            result['name'] = user.NAME
            user.LAST_LOGIN_TIME = int(round(time.time() * 1000))
            DAOUtils.commit()
            return Flask(__name__).make_response((jsonify(result), 200))
        else:
            return Flask(__name__).make_response(('', 404))

