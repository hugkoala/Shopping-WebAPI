from src.main import app;
from unittest import TestCase;
import unittest, json;
from hashlib import md5;
from src.dao.dao_utils import DAOUtils;


class TestAddOrder(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_add_order(self):
        db = DAOUtils.get_db()

        response = self.app.post('/order', data=json.dumps(dict(user_id='')),
                                 headers={"Content-Type": "application/json"})
        self.assertEqual(response.status_code, 404)

        account = 'leo.li'
        password = '123456'
        user = DAOUtils.get_user_dao().get_user(db, condition="ACCOUNT = '{ACCOUNT}' AND PASSWORD = '{PASSWORD}'",
                                                ACCOUNT=account,
                                                PASSWORD=md5(password.encode('utf-8')).hexdigest())

        body = dict(
            user_id=user.USER_ID
        )
        response = self.app.post('/order', data=json.dumps(body), headers={"Content-Type": "application/json"})
        if user:
            self.assertEqual(response.status_code, 201, 'Create Order Response Error')
        else:
            self.assertEqual(response.status_code, 404, 'User ID Not Found Response Error')


if __name__ == '__main__':
    unittest.main()
