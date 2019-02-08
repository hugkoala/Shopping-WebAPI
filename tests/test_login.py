from src.main import app;
from unittest import TestCase;
import unittest, json;
from hashlib import md5;
from src.dao.dao_utils import DAOUtils;


class TestLogin(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_login(self):
        db = DAOUtils.get_db()
        account = 'leo.li1'
        password = '123456'
        body = dict(
            account=account,
            password=password
        )
        user = DAOUtils.get_user_dao().get_user(db, condition="ACCOUNT = '{ACCOUNT}' AND PASSWORD = '{PASSWORD}'",
                                                ACCOUNT=account,
                                                PASSWORD=md5(password.encode('utf-8')).hexdigest())
        response = self.app.post('/login', data=json.dumps(body), headers={"Content-Type": "application/json"})
        if user:
            response_json = response.get_json()
            self.assertEqual(response_json['name'], user.NAME, 'Login Response User Name Error!')
            self.assertEqual(response_json['user_id'], user.USER_ID, 'Login Response User ID Error!')
        else:
            self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
