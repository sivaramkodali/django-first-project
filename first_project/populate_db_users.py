import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()


import random
from first_app.models import db_users
from faker import Faker

fakegen = Faker()

def populate(N=10):

    for entry in range(N):
        fake_name = fakegen.name().split()
        fake_fname = fake_name[0]
        fake_lname = fake_name[1]
        fake_email = fakegen.email()
        dbusers = db_users.objects.get_or_create(firstname=fake_fname,lastname=fake_lname,email=fake_email)[0]


if __name__ == '__main__':
    print("Populating Script!")
    populate(20)
    print("Populating Complete!")
