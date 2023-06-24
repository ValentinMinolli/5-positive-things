"""
Tests for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models

def create_user(email="testemail@example.com", password="password123"):
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
            ["test1@EXAMPLE.com", "test1@example.com"],
            ["Test2@Example.com", "Test2@example.com"],
            ["TEST3@EXAMPLE.COM", "TEST3@example.com"],
            ["test4@example.COM", "test4@example.com"],
            ["TeSt5@ExAmPlE.CoM", "TeSt5@example.com"],
        ]

        for email, expected in sample_mails:
            user = get_user_model().objects.create_user(email, "testpassword123")
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

    def test_create_five_positive_things(self):
        """Test creating five positive things is successfull."""
        user = get_user_model().objects.create_user(
            "testemail@example.com",
            "password123",
        )

        titles = ["Title 1", "Title 2", "Title 3", "Title 4", "Title 5"]
        descriptions = [
            "Description 1", 
            "Description 2", 
            "Description 3", 
            "Description 4", 
            "Description 5",
            ]

        positive_things = []
        for i in range(0, 4):
            positive_thing = models.PositiveThings.objects.create(
                user=user,
                title=titles[i],
                description=descriptions[i]
            )
            positive_things.append(positive_thing)

        
        self.assertEqual(len(positive_things), 5)
        self.assertEqual(positive_things[user], self.user)

        