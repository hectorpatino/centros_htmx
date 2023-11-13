from django.contrib.auth import get_user_model
from django.test import TestCase
from django.contrib.auth.hashers import check_password

User = get_user_model()


class TestUserManagers(TestCase):

    def test_create_user(self):
        email = "random_email@email.com"
        password = "foo"
        user = User.objects.create_user(
            email=email,
            password=password,
        )
        self.assertEqual(user.email, email)
        self.assertTrue(check_password("foo", user.password))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(ValueError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password=password)

    def test_create_superuser(self):
        email = "random_email@random.com"
        admin_user = User.objects.create_superuser(
            email=email,
            password="foo",
        )
        self.assertEqual(admin_user.email, email)
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        self.assertTrue(check_password("foo", admin_user.password))
        try:
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email=email,
                password="foo",
                is_superuser=False
            )
