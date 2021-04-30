import logging

logger = logging.getLogger(__name__)

with open("token.txt", "r") as r:
    readme = r.read()
