"""
Tests for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models

def create_user(email="test-email@example.com", password="password123"):
    """Create and return a new user."""
    return get_user_model().objects.create_user(email, password)

class ModelTests(TestCase):
    """Test models."""
    def test_create_user_with_email_successful(self):
        """Tests creating a user with email is successful."""
        email = "test@example.com"
        password = "password-example"
        user = get_user_model().objects.create_user(
            email = email,
            password = password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """Test email is normalize for new users."""
        sample_mails =[
            ["test123@EXAMPLE.com", "test123@example.com"],
            ["Test123@Example.com", "test123@example.com"],
            ["TEST123@EXAMPLE.COM", "test123@example.com"],
            ["test123@example.COM", "test123@example.com"],
            ["TeSt123@ExAmPlE.CoM", "test123@example.com"],
        ]

        for email, expected in sample_mails:
            user = get_user_model().objects.create_user(email, "test-password123")
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test that creating a user without email raises a ValueError."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user("", "test-password123")

    def test_create_superuser(self):
        """Test creating a superuser is successful."""
        superuser = get_user_model().objects.create_superuser(
            "testemail@example.com",
            "adminpassword123",
        )

        self.assertTrue(superuser.is_superuser)

        