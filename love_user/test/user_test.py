import unittest
import json
from rest_framework.test import APIClient
from rest_framework import status
from faker import Faker
from core.utils.setup import logger, readme, writeTest, interested
from django.contrib.auth.models import User
from django.urls import reverse
import os
import cowsay
from django.core.files import File
import random

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
        writeTest("- User Create : \n")
        writeTest(str(response.data))
        writeTest("\n")
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
        writeTest("- Token : \n")
        writeTest(str(response.data))
        writeTest("\n")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data, None)
        logger.info("User Login")

    @unittest.skipIf(not readme, "Skip! missing token")
    def test_usr_refresh(self):
        urls = reverse("authtoken-refresh")
        data = json.dumps({"token": readme})
        response = self.e.post(urls, data, content_type="application/json")
        writeTest("- Refresh Token : \n")
        writeTest(str(response.data))
        writeTest("\n")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data, None)
        logger.info("Refresh Token")

    @unittest.skipIf(not readme, "Skip! missing token")
    def test_usr_verify(self):
        urls = reverse("authtoken-verify")
        data = json.dumps({"token": readme})
        response = self.e.post(urls, data, content_type="application/json")
        writeTest("- Verify Token : \n")
        writeTest(str(response.data))
        writeTest("\n")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data, None)
        logger.info("Verify Token")

    @unittest.skipIf(User.objects.count() == 0, "Skip! User not have data")
    def test_usr_reset(self):
        user = User.objects.last()
        urls = reverse("user-reset")
        data = json.dumps({"token": user.email})
        response = self.e.post(urls, data, content_type="application/json")
        writeTest("- User Reset : \n")
        writeTest(str(response.data))
        writeTest("\n")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data, None)
        logger.info("User Reset")

    @unittest.skipIf(not readme, "Skip! missing token")
    def test_usr_generic_list(self):
        urls = reverse("user-generic-list")
        self.e.credentials(HTTP_AUTHORIZATION="Bearer " + readme)
        response = self.e.get(urls, content_type="application/json")
        writeTest("- User List Generics : \n")
        writeTest(str(response.data[0:2]))
        writeTest("\n")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data, None)
        logger.info("User List Generics")

    @unittest.skipIf(not readme, "Skip! missing token")
    def test_usr_filter_generic_list(self):
        user = User.objects.filter(first_name__gt=1).last()
        urls = reverse("user-generic-list")
        urls_prefix = "%s?first_name=%s" % (urls, user.first_name)
        self.e.credentials(HTTP_AUTHORIZATION="Bearer " + readme)
        response = self.e.get(urls_prefix, content_type="application/json")
        writeTest("- User List Generics Filter : \n")
        writeTest(str(response.data))
        writeTest("\n")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data, None)
        logger.info("User List Generics - Filter")

    def test_usr_list(self):
        urls = reverse("user-list")
        response = self.e.get(urls, content_type="application/json")
        writeTest("- User List: \n")
        if len(response.data) < 1:
            writeTest(str(response.data))
        else:
            writeTest(str(response.data[0:1]))
        writeTest("\n")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        logger.info("User List")

    @unittest.skipIf(not readme, "Skip! missing token")
    def test_usr_update(self):
        urls = reverse("user-update")
        files = File(open("image_test.jpeg", "rb"))
        data = {
            "first_name": fake.name(),
            "last_name": fake.name(),
            "avatar": files,
            "phone_numbers": "+628%s" % (random.randint(929349, 999999) * 999),
            "gender": random.randint(0, 1),
            "country": fake.country(),
            "province": fake.state(),
            "city": fake.city(),
            "address": fake.address(),
        }
        self.e.credentials(HTTP_AUTHORIZATION="Bearer " + readme)
        response = self.e.post(urls, data, follow=True)
        writeTest("- Update Accounts : \n")
        writeTest(str(response.data))
        writeTest("\n")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data, None)
        logger.info("Update Accounts")

    @unittest.skipIf(
        not readme and User.objects.filter(first_name__gt=1).count() == 0,
        "Skip! missing token or User not have first_name",
    )
    def test_usr_detail(self):
        user = User.objects.filter(first_name__gt=1).first()
        urls = reverse("user-detail", args=[user.id])
        self.e.credentials(HTTP_AUTHORIZATION="Bearer " + readme)
        response = self.e.get(urls, content_type="application/json")
        writeTest("- User Detail : \n")
        writeTest(str(response.data))
        writeTest("\n")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        logger.info("User Detail")

    @unittest.skipIf(not readme, "Skip! missing token")
    def test_usr_bio_update(self):
        urls = reverse("user-bio-update")
        data = json.dumps(
            {
                "bio": fake.text(),
                "name": interested["list"][random.randint(0, 1)]["choice"][
                    random.randint(0, 10)
                ],
            }
        )
        self.e.credentials(HTTP_AUTHORIZATION="Bearer " + readme)
        response = self.e.post(urls, data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        logger.info("Accounts bio updated")

    @classmethod
    def tearDownClass(cls):
        cowsay.dragon("Running unit tester has finished")
        os.system("cat test.log")
