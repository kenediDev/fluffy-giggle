import unittest
import json
from rest_framework.test import APIClient
from rest_framework import status
from faker import Faker
from core.utils.setup import logger, readme
from django.contrib.auth.models import User
from django.urls import reverse

fake = Faker()


class UserTester(unittest.TestCase):
    def setUp(self):
        self.e = APIClient()

    def test_usr_a_(self):
        logger.critical("User Tester")

    def test_usr_create(self):
        urls = reverse("user-list")
        data = json.dumps(
            {
                "username": fake.name(),
                "email": fake.email(),
                "password": "Password",
                "confirm_password": "Password",
            }
        )
        response = self.e.post(urls, data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        logger.info(response.data.get("message"))

    @unittest.skipIf(User.objects.count() == 0, "Skip! User not have data")
    def test_usr_login(self):
        user = User.objects.last()
        urls = reverse("authtoken")
        data = json.dumps({"username": user.username, "password": "Password"})
        response = self.e.post(urls, data, content_type="application/json")
        with open("token.txt", "w") as w:
            w.write(response.data.get("token"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data, None)
        logger.info("User Login")

    @unittest.skipIf(not readme, "Skip! missing token")
    def test_usr_refresh(self):
        urls = reverse("authtoken-refresh")
        data = json.dumps({"token": readme})
        response = self.e.post(urls, data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data, None)
        logger.info("Refresh Token")

    @unittest.skipIf(not readme, "Skip! missing token")
    def test_usr_verify(self):
        urls = reverse("authtoken-verify")
        data = json.dumps({"token": readme})
        response = self.e.post(urls, data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data, None)
        logger.info("Verify Token")

    @unittest.skipIf(User.objects.count() == 0, "Skip! User not have data")
    def test_usr_reset(self):
        user = User.objects.last()
        urls = reverse("user-reset")
        data = json.dumps({"token": user.email})
        response = self.e.post(urls, data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data, None)
        logger.info("User Reset")
