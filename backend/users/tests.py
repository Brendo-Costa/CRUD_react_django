"""Tests for users app."""

from django.test import TestCase
from django.contrib.auth import get_user_model




class ModelTests(TestCase):
    """Test models."""
    
    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is susscessful."""
        
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create(
            email = email,
            password = password,
        )
        total = len(get_user_model().objects.all())

        self.assertEqual(user.email, email)
        self.assertTrue(user.password, password)
        self.assertEqual(total, 1)