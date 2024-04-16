from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create(
            username="TonyStark", email="ironman@avengers.com", password="a$$emble!"
        )

        self.assertEqual(user.username, "TonyStark")
        self.assertEqual(user.email, "ironman@avengers.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username="BruceWayne", email="batman@justiceleague.com", password="AlfredisCool420?"
        )

        self.assertEqual(user.username, "BruceWayne")
        self.assertEqual(user.email, "batman@justiceleague.com")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_superuser)