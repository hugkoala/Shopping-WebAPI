from flask import request, Flask;


class Users:

    @staticmethod
    def add_user():
        print(request.get_json())
        return Flask(__name__).make_response(('', 201))
