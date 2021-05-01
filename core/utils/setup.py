import logging
import json

logger = logging.getLogger(__name__)

with open("token.txt", "r") as r:
    readme = r.read()


def writeTest(args):
    with open("test.log", "a+") as w:
        w.write(args)


with open("valueable/interested.json", "r") as r:
    interested = json.loads(r.read())
