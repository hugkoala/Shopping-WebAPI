from src.main import app;
from unittest import TestCase;
import unittest, json;
from hashlib import md5;
from src.dao.dao_utils import DAOUtils;


class TestAddCart(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_add_cart(self):
        db = DAOUtils.get_db()

        response = self.app.post('/cart', data=json.dumps(dict(user_id='', item_id=0, amount=0)),
                                 headers={"Content-Type": "application/json"})
        self.assertEqual(response.status_code, 404, 'User ID Empty Response Error')

        account = 'leo.li'
        password = '123456'
        user = DAOUtils.get_user_dao().get_user(db, condition="ACCOUNT = '{ACCOUNT}' AND PASSWORD = '{PASSWORD}'",
                                                ACCOUNT=account,
                                                PASSWORD=md5(password.encode('utf-8')).hexdigest())

        user_id = user.USER_ID
        item_id = 1
        amount = 10

        item = DAOUtils.get_product_dao().get_product(db, condition="ITEM_ID = '{ITEM_ID}'", ITEM_ID=item_id)
        cart = DAOUtils.get_cart_dao().get_carts(db, condition="USER_ID = '{USER_ID}' AND ITEM_ID = '{ITEM_ID}'",
                                                 USER_ID=user_id, ITEM_ID=item_id)

        response = self.app.post('/cart', data=json.dumps(dict(
            user_id=user_id,
            item_id=item_id,
            amount=amount
        )), headers={"Content-Type": "application/json"})

        if item:
            if cart and cart[0]:
                self.assertEqual(response.status_code, 406, 'Cart Existed Response Error')
            else:
                self.assertEqual(response.status_code, 201, 'Cart Add Response Error')
        else:
            self.assertEqual(response.status_code, 406, 'Item Not Found Response Error')

        amount = 999999999
        response = self.app.post('/cart', data=json.dumps(dict(
            user_id=user_id,
            item_id=item_id,
            amount=amount
        )), headers={"Content-Type": "application/json"})

        self.assertEqual(response.status_code, 403, 'Item Amount Not Enough Response Error')


if __name__ == '__main__':
    unittest.main()
