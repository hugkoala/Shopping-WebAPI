from flask import Flask, request;
from users import Users;


users = Users()

app = Flask(__name__)


@app.route('/user', methods=['POST'])
def add_user():
    return users.add_user()


if __name__ == '__main__':
    app.run(debug=True)
