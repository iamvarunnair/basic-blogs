from django.db import models
from datetime import datetime

# Create your models here.


class BOUserStatus (models.Model):
    status_id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=100, blank=True)
    added_by = models.CharField(max_length=100, default=None)
    added_date = models.DateTimeField(default=datetime.now)
    last_modified_by = models.CharField(max_length=100, default=None)
    last_modified_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.status_id)


class BOUser(models.Model):
    bo_user_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    added_by = models.CharField(max_length=100, default=None)
    added_date = models.DateField(default=datetime.now)
    last_modified_by = models.CharField(max_length=100, default=None)
    last_modified_date = models.DateField(default=datetime.now)
    status = models.ForeignKey(
        BOUserStatus, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.bo_user_id)
