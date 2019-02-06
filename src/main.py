from flask import Flask;
from user_handler import UserHandler;
from users_handler import UsersHandler;
from cart_handler import CartHandler;
from carts_handler import CartsHandler;
from order_handler import OrderHandler;
from login import Login;
from threading import Lock;


app = Flask(__name__)
lock = Lock()


# 會員登入
@app.route('/login', methods=['POST'])
def login():
    with lock:
        return Login.login()


# 註冊
@app.route('/users', methods=['POST'])
def add_user():
    with lock:
        return UsersHandler.add_user()


# 查詢會員資料
@app.route('/user/<account>', methods=['GET'])
def get_user(account):
    return UserHandler.get_user(account)


# 會員增加額度
@app.route('/user/credit', methods=['POST'])
def add_credit():
    with lock:
        return UserHandler.add_credit()


# 查詢會員操作日誌
@app.route('/user/action_log/<user_id>', methods=['GET'])
def get_user_log(user_id):
    return UserHandler.get_user_log(user_id)


# 商品加入至購物車、購物車移除商品
@app.route('/cart', methods=['POST', 'DELETE'])
def cart_handler():
    with lock:
        return CartHandler.cart_handler()


# 查詢購物車項目列表
@app.route('/carts', methods=['GET'])
def carts_handler():
    return CartsHandler.carts_handler()


# 購物車結帳
@app.route('/order', methods=['POST'])
def check_out_to_order():
    with lock:
        return OrderHandler.cart_to_order()


if __name__ == '__main__':
    app.run(debug=True)

