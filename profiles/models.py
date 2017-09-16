from django.db import models
from django.contrib.auth.models import User
from cars.models import Build
from enum import Enum, unique
from cardb.helpers import django_enum
import uuid

class UserProfile(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user = models.OneToOneField(User, null=True, blank=True)
    last_seen_timestamp = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    first_seen_timestamp = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    session_count = models.IntegerField(default=1, null=False, blank=False)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        if self.user is None:
            return "Guest UserProfile - %d" % self.id
        else:
            return "%s (%d)" % (self.user.username, self.id)


class UserBuildImpression(models.Model):
    user_profile = models.ForeignKey(UserProfile)
    build = models.ForeignKey(Build)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "UserProfile %d : %s (%d)" % (self.user_profile.id, self.build.name, self.build.id)


class UserBuildView(models.Model):
    user_profile = models.ForeignKey(UserProfile)
    build = models.ForeignKey(Build)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "UserProfile %d : %s (%d)" % (self.user_profile.id, self.build.name, self.build.id)

class Session(models.Model):

    @unique
    @django_enum
    class SessionPlatform(Enum):
        WEB = '1'
        IOS = '2'
        ANDROID = '3'
        OTHER = '0'

    id = models.UUIDField(primary_key=True,default=uuid.uuid4())
    user_profile = models.ForeignKey(UserProfile)
    start_timestamp = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    latest_request_timestamp = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    platform = models.CharField(max_length=1, choices = [(choice.value, choice.name) for choice in SessionPlatform])

    def __str__(self):
        return "%d - %s" % (self.user_profile.id, self.start_timestamp)

class PageView(models.Model):
    user_profile = models.ForeignKey(UserProfile)
    session = models.ForeignKey(Session, null=True, blank=True)
    path = models.TextField(null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def __str__(self):
        return "%d : %s - %s" % (self.user_profile.id, self.path, self.timestamp)