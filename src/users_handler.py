from flask import request, Flask;
from dao.models import DAO;
from dao.dao_utils import DAOUtils;
from dao.dborm import User


class UsersHandler:

    @staticmethod
    def add_user():
        input_json = request.get_json()
        user = User(account=input_json['account'], pwd=input_json['password'], name=input_json['name'],
                    credit=input_json['credit'])
        DAOUtils.get_user_dao().insert_user(user)
        DAO.commit()
        return Flask(__name__).make_response(('', 201))
