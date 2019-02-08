from src.main import app;
from unittest import TestCase;
import unittest, json;
from hashlib import md5;
from src.dao.dao_utils import DAOUtils;


class TestAddUserCredit(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_add_user_credit(self):
        db = DAOUtils.get_db()

        response = self.app.post('/user/credit', data=json.dumps(dict(user_id='', amount=0)),
                                 headers={"Content-Type": "application/json"})
        self.assertEqual(response.status_code, 404)

        account = 'leo.li'
        password = '123456'
        user = DAOUtils.get_user_dao().get_user(db, condition="ACCOUNT = '{ACCOUNT}' AND PASSWORD = '{PASSWORD}'",
                                                ACCOUNT=account,
                                                PASSWORD=md5(password.encode('utf-8')).hexdigest())

        if user:
            user_id = user.USER_ID
            amount = 296
            response = self.app.post('/user/credit', data=json.dumps(dict(user_id=user_id, amount=amount)),
                                     headers={"Content-Type": "application/json"})
            response_json = response.get_json()
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response_json['name'], user.NAME, 'Add User Credit Response User Name Error!')
            self.assertEqual(response_json['user_id'], user.USER_ID, 'Add User Credit Response User ID Error!')
        else:
            self.assertEqual(response.status_code, 406)


if __name__ == '__main__':
    unittest.main()
