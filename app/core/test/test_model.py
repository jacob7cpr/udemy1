from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """ test creating a new user with email DONE """
        email = 'test@shark.com'
        password = 'testPas123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test email for new user """
        email = 'liilhkj@TEST.COM'
        user = get_user_model().objects.create_user(email, 'TestPas1223')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ test creating user with no valid emial """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test1234')

    def test_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@londonappdev.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
