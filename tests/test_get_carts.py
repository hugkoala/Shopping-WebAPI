from src.main import app;
from unittest import TestCase;
import unittest, json;
from hashlib import md5;
from src.dao.dao_utils import DAOUtils;
from tests.assertions import assert_valid_schema;


class TestGetCarts(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_carts(self):
        db = DAOUtils.get_db()

        response = self.app.get('/carts', data=json.dumps(dict(user_id='')),
                                 headers={"Content-Type": "application/json"})
        self.assertEqual(response.status_code, 404, 'User ID Empty Response Error')

        account = 'leo.li'
        password = '123456'
        user = DAOUtils.get_user_dao().get_user(db, condition="ACCOUNT = '{ACCOUNT}' AND PASSWORD = '{PASSWORD}'",
                                                ACCOUNT=account,
                                                PASSWORD=md5(password.encode('utf-8')).hexdigest())

        user_id = user.USER_ID

        cart = DAOUtils.get_cart_dao().get_carts(db, condition="USER_ID = '{USER_ID}'", USER_ID=user_id)

        response = self.app.get('/carts', data=json.dumps(dict(
            user_id=user_id
        )), headers={"Content-Type": "application/json"})

        self.assertEqual(response.status_code, 200, 'Cart Get Response Error')
        if cart and cart[0]:
            assert_valid_schema(response.get_json(), 'test_get_carts.json')
        else:
            self.assertIn('total', response.get_json(), 'Cart Response not found total key')
            self.assertIn('item_list', response.get_json('Cart Response not found item_list key'))





if __name__ == '__main__':
    unittest.main()
