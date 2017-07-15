from django.db import models

# Create your models here.


class topic(models.Model):
    top_name = models.CharField(blank=True, max_length=100,unique=True)


    def __str__(self):
        return self.top_name


class webpage(models.Model):
    topic = models.ForeignKey(topic)
    name = models.CharField(max_length=100,unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class accessrecord(models.Model):
    name = models.ForeignKey(webpage)
    date = models.DateField()

    def __str__(self):
        return str(self.date)


class db_users(models.Model):
    firstname = models.CharField(blank=True, max_length=100)
    lastname = models.CharField(blank=True, max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return str(self.email)

from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User)
    #additional attributes
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to="profile_pics", blank=True)

    def __str__(self):
        return self.user.username
