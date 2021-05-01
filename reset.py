import os

os.system("rm db.sqlite3")
os.system("python manage.py migrate")
with open("token.txt",'w') as w:
    w.write("")
os.system("python manage.py test")
