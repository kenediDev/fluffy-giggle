import unittest
import coloredlogs
import logging
import sys
from love_user.test.user_test import UserTester
from love_post.test.post_test import PostTester

coloredlogs.install()

logging.basicConfig(level=logging.DEBUG,stream=sys.stdout,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    unittest.main()
