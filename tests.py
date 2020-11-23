import unittest
from app.models import usuario_model


class UserModelCase(unittest.TestCase):
    def test_password_hashing(self):
        u = usuario_model.User(username='admin', email='admin@admin.com', is_admin=True)
        u.set_password('@admin.admin')
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('@admin.admin'))


if __name__ == '__main__':
    unittest.main()
