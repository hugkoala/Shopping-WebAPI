from src.main import app;
from unittest import TestCase;
import unittest, json, uuid;
from src.dao.dao_utils import DAOUtils;


class TestAddUser(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_add_user(self):
        db = DAOUtils.get_db()

        response = self.app.post('/users', data=json.dumps(dict(account='', password='', name='', credit=0)),
                                 headers={"Content-Type": "application/json"})
        self.assertEqual(response.status_code, 406)

        account = 'leo.li'
        password = '123456'
        name = 'Leo.Li'
        credit = 20000
        body = dict(
            account=account,
            password=password,
            name=name,
            credit=credit
        )
        user = DAOUtils.get_user_dao().get_user(db, condition="ACCOUNT = '{ACCOUNT}'",
                                                ACCOUNT=account)

        response = self.app.post('/users', data=json.dumps(body), headers={"Content-Type": "application/json"})
        if user:
            self.assertEqual(response.status_code, 406, 'User Existed Response Error')
        else:
            self.assertEqual(response.status_code, 201, 'User Created Response Error')

        account = name = str(uuid.uuid4())[0:20]

        response = self.app.post('/users', data=json.dumps(dict(account=account, password=password,
                                                                name=name, credit=credit)),
                                 headers={"Content-Type": "application/json"})
        self.assertEqual(response.status_code, 201, 'User Created Response Error')


if __name__ == '__main__':
    unittest.main()
