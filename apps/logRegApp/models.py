from __future__ import unicode_literals
from django.db import models
from datetime import date
import re
import string
import bcrypt

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors ={}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid Email"
        if len(postData['firstName'])<2:
            errors['firstNameLength'] = "First name must be at least 2 characters"
        if postData['firstName'].isalpha()==False:
            errors['firstNameChar'] = "First name must contain only letters"
        if len(postData['lastName'])<2:
            errors['lastName'] = "Last name must be at least 2 characters"
        if postData['lastName'].isalpha()==False:
            errors['lastNameChar'] = "Last name must contain only letters"
        if len(postData['password'])<8:
            errors['passwordLen'] = "Password must be 8 characters long"
        if postData['password'] != postData['confPassword']:
            errors['passwordMatch'] = "Password must match Confirm Password field"
        return errors

class User(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=40)
    username = models.CharField(max_length=65)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=80)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    objects = UserManager()


