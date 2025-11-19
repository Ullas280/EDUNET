from django.db import models
from django.conf import settings


class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    jobType = models.CharField(max_length=50, blank=True, null=True)
    salary = models.CharField(max_length=50, blank=True, null=True)
    experience = models.IntegerField(blank=True, null=True)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='jobs')
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='applications')
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant} -> {self.job}"
