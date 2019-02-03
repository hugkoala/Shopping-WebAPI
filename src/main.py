from flask import Flask, request, jsonify, json;
from flask_sqlalchemy import SQLAlchemy;
from user_handler import UserHandler;
from users_handler import UsersHandler;
from login import Login;


app = Flask(__name__)


# 會員登入
@app.route('/login', methods=['POST'])
def login():
    return Login.login()


# 註冊
@app.route('/users', methods=['POST'])
def add_user():
    return UsersHandler.add_user()


@app.route('/user/<account>', methods=['GET'])
def get_user(account):
    return UserHandler.get_user(account)


@app.route('/user', methods=['DELETE'])
def delete_user(id):
    pass


if __name__ == '__main__':
    app.run(debug=True)

