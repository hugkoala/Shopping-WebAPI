from flask import Flask, request, jsonify, json;
from flask_sqlalchemy import SQLAlchemy;
from user_handler import UserHandler;
from users_handler import UsersHandler;
from cart_handler import CartHandler;
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


# 查詢會員資料
@app.route('/user/<account>', methods=['GET'])
def get_user(account):
    return UserHandler.get_user(account)


# 商品加入至購物車
@app.route('/cart', methods=['POST'])
def add_cart():
    return CartHandler.add_cart()

if __name__ == '__main__':
    app.run(debug=True)

