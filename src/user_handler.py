from flask import Flask, jsonify, request, json;
from src.dao.dao_utils import DAOUtils;
from src.log_utils import LogUtils;
import sys;


class UserHandler:

    @staticmethod
    def get_user(account):
        """
        Get User Info
        :param account:the account of user
        :return:Response
        """
        db = DAOUtils.get_db()
        user = DAOUtils.get_user_dao().get_user(db, "ACCOUNT = '{ACCOUNT}'", ACCOUNT=account)
        if user:
            result = dict()
            result['account'] = user.ACCOUNT
            result['name'] = user.NAME
            result['credit'] = int(user.CREDIT)
            result['created_time'] = int(user.CREATED_TIME)
            result['last_login_time'] = int(user.LAST_LOGIN_TIME)
            DAOUtils.close(db)
            return Flask(__name__).make_response((jsonify(result), 200))
        else:
            DAOUtils.close(db)
            return Flask(__name__).make_response(('', 404))

    @staticmethod
    def add_credit():
        """
        Add User Credit
        :return:Response
        """
        db = DAOUtils.get_db()
        input_json = request.get_json()
        user = DAOUtils.get_user_dao().get_user(db, "USER_ID = '{USER_ID}'", USER_ID=input_json['user_id'])
        if user:
            try:
                user.CREDIT += input_json['amount']
                LogUtils.insert_user_log(db, user_id=input_json['user_id'],
                                         action='會員存款', remark=str(json.dumps(input_json)))
                DAOUtils.commit(db)
                result = dict()
                result['user_id'] = user.USER_ID
                result['name'] = user.NAME
                return Flask(__name__).make_response((jsonify(result), 200))
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
    def get_user_log(user_id):
        """
        Get User Action Log
        :param user_id:the user_id of user
        :return:Response
        """
        db = DAOUtils.get_db()
        user = DAOUtils.get_user_dao().get_user(db, "USER_ID = '{USER_ID}'", USER_ID=user_id)
        if user:
            result = dict()
            result['account'] = user.ACCOUNT
            result['name'] = user.NAME
            result['action_list'] = list()

            for user_log in user.USER_LOGS:
                action_item = dict()
                action_item['action'] = user_log.ACTION
                action_item['created_time'] = int(user_log.CREATED_TIME)
                action_item['remarks'] = user_log.REMARK
                result['action_list'].append(action_item)
            DAOUtils.close(db)
            return Flask(__name__).make_response((jsonify(result), 200))
        else:
            DAOUtils.close(db)
            return Flask(__name__).make_response(('', 404))





