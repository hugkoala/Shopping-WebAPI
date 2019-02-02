from flask import request, Flask, jsonify;
# from dao.models import DAO;
from dao.dao_utils import DAOUtils;
from dao.dborm import User;
import sys;


class UsersHandler:

    @staticmethod
    def add_user():
        input_json = request.get_json()
        user = User(account=input_json['account'], pwd=input_json['password'], name=input_json['name'],
                    credit=input_json['credit'])
        try:
            DAOUtils.get_user_dao().insert_user(user)
            DAOUtils.commit()
            return Flask(__name__).make_response(('', 201))
        except:
            DAOUtils.rollback()
            error_result = dict()
            error_result['error'] = str(sys.exc_info())
            return Flask(__name__).make_response((jsonify(error_result), 406))
