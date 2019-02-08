from src.main import app;
from unittest import TestCase;
import unittest;
from src.dao.dao_utils import DAOUtils;
from tests.assertions import assert_valid_schema;
from hashlib import md5;


class TestGetUserActionLog(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_user_action_log(self):
        db = DAOUtils.get_db()

        response = self.app.get('/user/action_log/', headers={"Content-Type": "application/json"})
        self.assertEqual(response.status_code, 404, 'User ID Empty Response Error')

        account = 'leo.li'
        password = '123456'
        user = DAOUtils.get_user_dao().get_user(db, condition="ACCOUNT = '{ACCOUNT}' AND PASSWORD = '{PASSWORD}'",
                                                ACCOUNT=account,
                                                PASSWORD=md5(password.encode('utf-8')).hexdigest())

        response = self.app.get('/user/action_log/' + user.USER_ID, headers={"Content-Type": "application/json"})
        self.assertEqual(response.status_code, 200, 'User Get Response Error')
        if user.USER_LOGS:
            assert_valid_schema(response.get_json(), 'test_get_user_action_log.json')
        else:
            self.assertIn('account', response.get_json(), 'User Action Log Response not found account key')
            self.assertIn('name', response.get_json(), 'User Action Log Response not found name key')
            self.assertIn('action_list', response.get_json(), 'User Action Log Response not found action_list key')


if __name__ == '__main__':
    unittest.main()
