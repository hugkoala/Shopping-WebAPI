from flask import Flask, request, jsonify, json;
from user_handler import UserHandler;
from users_handler import UsersHandler;
from cart_handler import CartHandler;
from order_handler import OrderHandler;
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


# 商品加入至購物車、購物車移除商品、查詢購物車項目列表
@app.route('/cart', methods=['GET', 'POST', 'DELETE'])
def cart_handler():
    return CartHandler.cart_handler()


# 購物車結帳
@app.route('/order', methods=['POST'])
def check_out_to_order():
    return OrderHandler.cart_to_order()


if __name__ == '__main__':
    app.run(debug=True)

