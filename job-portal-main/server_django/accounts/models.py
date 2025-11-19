from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None
    fullname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phoneNumber = models.CharField(max_length=30)

    STUDENT = 'student'
    RECRUITER = 'recruiter'
    ROLE_CHOICES = [
        (STUDENT, 'Student'),
        (RECRUITER, 'Recruiter'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    profile_bio = models.TextField(blank=True, null=True)
    profile_skills = models.JSONField(blank=True, null=True)
    profile_resume = models.URLField(blank=True, null=True)
    profile_resumeOriginalName = models.CharField(max_length=255, blank=True, null=True)
    profile_profilePhoto = models.URLField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
