import unittest
from django.urls import reverse
from core.utils.setup import logger, readme, writeTest
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_jwt.settings import api_settings
from django.core.files import File
from faker import Faker
from database.models.post import Post

fake = Faker()

class PostTester(unittest.TestCase):
    def setUp(self):
        self.e = APIClient()
        self.decode = api_settings.JWT_DECODE_HANDLER
        self.payload = self.decode(readme)


    def test_post_a(self):
        logger.critical("Post Tester")

    @unittest.skipIf(not readme, "Skip! missing Token")
    def test_post_create(self):
        urls = reverse("post-list")
        files = File(open("image_test.jpeg","rb"))
        data = {
                "content": fake.text(),
                "photo": files,
                "author": self.payload.get("user_id")
                }
        self.e.credentials(HTTP_AUTHORIZATION="Bearer " + readme)
        response = self.e.post(urls,data,follow=True)
        writeTest("- Create Post: \n")
        writeTest("Post has been created")
        writeTest("\n")
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertNotEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        logger.info("Post has been created")

    def test_post_list(self):
        urls = reverse('post-list')
        response = self.e.get(urls,content_type='application/json')
        writeTest("- Post List: \n")
        if len(response.data) < 3:
            writeTest(str(response.data))
        else:
            writeTest(str(response.data[0:1]))
        writeTest("\n")
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertNotEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        logger.info("Post List")

    @unittest.skipIf(Post.objects.count() == 0 and not readme, "Skip! missing token or Post not have data")
    def test_post_detail(self):
        post = Post.objects.last()
        urls = reverse('post-detail', args=[post.public_id])
        response = self.e.get(urls,content_type='application/json')
        writeTest("- Post Detail: \n")
        writeTest(str(response.data))
        writeTest("\n")
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertNotEqual(response.status_code,status.HTTP_404_NOT_FOUND)
        logger.info("Post Detail")

    @unittest.skipIf(Post.objects.count() == 0 and not readme, "Skip! missing token or Post not have data")
    def test_post_update(self):
        post = Post.objects.last()
        urls = reverse('post-update', args=[post.public_id])
        files = File(open("image_test.jpeg","rb"))
        data = {
                "content": fake.text(),
                "photo": files}
        self.e.credentials(HTTP_AUTHORIZATION="Bearer "+ readme)
        response = self.e.post(urls,data,follow=True)
        writeTest("- Post Update: \n")
        writeTest(str(response.data))
        writeTest("\n")
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertNotEqual(response.status_code,status.HTTP_404_NOT_FOUND)
        logger.info("Post Update")

    @unittest.skipIf(Post.objects.count() ==0, "Skip! Post not have data")
    def test_post_generics_list(self):
        post = Post.objects.first()
        urls = reverse('post-generics-list')
        urls_prefix = "%s?content=%s" % (urls,post.content[0:5])
        response = self.e.get(urls_prefix,content_type='application/json') 
        writeTest("- Post Generics Filter: \n")
        writeTest(str(response.data))
        writeTest("\n")
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertNotEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        logger.info("Post List Generics - Filter")





