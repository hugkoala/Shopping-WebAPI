from flask import Flask, jsonify, request;
from dao.dao_utils import DAOUtils;
from threading import Lock;

lock = Lock()


class UserHandler:

    @staticmethod
    def get_user(account):
        user = DAOUtils.get_user_dao().get_user("ACCOUNT = '{ACCOUNT}'", ACCOUNT=account)
        result = dict()
        result['account'] = user.ACCOUNT
        result['name'] = user.NAME
        result['credit'] = user.CREDIT
        result['created_time'] = int(user.CREATED_TIME)
        result['last_login_time'] = int(user.LAST_LOGIN_TIME)
        return Flask(__name__).make_response((jsonify(result), 200))

    @staticmethod
    def add_credit():
        input_json = request.get_json()
        user = DAOUtils.get_user_dao().get_user("USER_ID = '{USER_ID}'", USER_ID=input_json['user_id'])
        with lock:
            if user:
                try:
                    user.CREDIT += input_json['amount']
                    DAOUtils.commit()
                    result = dict()
                    result['user_id'] = user.USER_ID
                    result['name'] = user.NAME
                    return Flask(__name__).make_response((jsonify(result), 200))
                except:
                    DAOUtils.rollback()
                    error_result = dict()
                    error_result['error'] = str(sys.exc_info())
                    return Flask(__name__).make_response((jsonify(error_result), 406))
            else:
                return Flask(__name__).make_response(('', 404))





