from src.main import app;
from unittest import TestCase;
import unittest;
from src.dao.dao_utils import DAOUtils;
from tests.assertions import assert_valid_schema;


class TestGetUser(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_user(self):
        db = DAOUtils.get_db()

        response = self.app.get('/user/', headers={"Content-Type": "application/json"})
        self.assertEqual(response.status_code, 404, 'User Account Empty Response Error')

        account = 'leo.li'
        user = DAOUtils.get_user_dao().get_user(db, condition="ACCOUNT = '{ACCOUNT}'",
                                                ACCOUNT=account)

        response = self.app.get('/user/' + account, headers={"Content-Type": "application/json"})

        if user:
            self.assertEqual(response.status_code, 200, 'User Get Response Error')
            assert_valid_schema(response.get_json(), 'test_get_user.json')
        else:
            self.assertEqual(response.status_code, 404, 'User Account Not Found Response Error')
            self.assertIn('total', response.get_json(), 'Cart Response not found total key')
            self.assertIn('item_list', response.get_json('Cart Response not found item_list key'))


if __name__ == '__main__':
    unittest.main()
