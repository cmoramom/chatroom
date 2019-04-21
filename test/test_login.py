import unittest


from dao import user


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.auth = user.User()
        self.auth.user = 'user2Chat'
        self.auth.password = 'user2Chat'

    def test_login_ok(self):
        self.assertEqual(self.auth.verify_user(), True)

    def test_login_fail(self):
        self.auth.password = 'WrongPass'
        self.assertFalse(self.auth.verify_user(), False)


if __name__ == '__main__':
    unittest.main()
