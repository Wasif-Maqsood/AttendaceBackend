import os
import random
import string
import uuid
from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser, BaseUserManager
from datetime import datetime
import json
import urllib.request
# from geopy.geocoders import Nominatim

def image_name_and_path(instance, image_name):
    """Replace the image name with random string and return the path and name"""
    ext = image_name.split(".")[-1]  # Get the extension of the image
    random_string = "".join(
        random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
        for _ in range(33)
    )
    # Replace the image name with random string
    image_name = "%s.%s" % (random_string, ext)

    return os.path.join("accounts/", image_name)


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError("The given email must be set")
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)

class Location(models.Model):
    def location_lookup():
  
        return json.load( urllib.request.urlopen('http://ipinfo.io/json'))
    location = location_lookup()

    # print city and latitude/longitude
    lat_=location['city']  
    long_=location['loc']
    x = long_.split(",")
    latetude=x[0]
    longitude=x[1]
    #print(type(long_))
    #print(longitude)
    # calling the nominatim tool
    #geoLoc = Nominatim(user_agent="GetLoc")
    
    # passing the coordinates
    #locname = geoLoc.reverse(long_)
    locname="Lahore"
    location_id = models.AutoField(
        primary_key=True, unique=True, editable=False
    )                                      
    lat = models.FloatField(default=latetude)
    lon = models.FloatField(default=longitude)
    address = models.CharField(default=lat_,max_length=500)
    city = models.CharField(default=lat_,max_length=50)
class User(AbstractUser):
    username = None
    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False
    )
    avatar = models.ImageField(upload_to=image_name_and_path, blank=True, null=True)
    name = models.CharField(max_length=160)
    email = models.EmailField(_("email address"), unique=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    objects = UserManager()

    def __str__(self):
        return self.name
class Employee(models.Model):
    username = None
    id = models.AutoField(primary_key=True)
    avatar = models.ImageField(upload_to=image_name_and_path, blank=True, null=True)
    name = models.CharField(max_length=160)
    email = models.EmailField(_("email address"), unique=True)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)
    password = models.CharField(max_length=50)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    objects = UserManager()

    def __str__(self):
        return self.name

class Attendance(models.Model):
    attendance_id = models.AutoField(
        primary_key=True, unique=True, editable=False
    )
    time_in = models.DateTimeField(blank=True)
    time_out = models.DateTimeField(blank=True,null=True)
    user_id = models.ForeignKey(Employee, on_delete=models.CASCADE)



