from flask import Flask, jsonify;
from dao.dao_utils import DAOUtils;


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



