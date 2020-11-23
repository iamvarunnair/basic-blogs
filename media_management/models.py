from django.db import models
from datetime import datetime, timedelta

# Create your models here.


class MediaStatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=100, default="not defined")
    added_by = models.CharField(max_length=100, default=None)
    added_date = models.DateTimeField(default=datetime.now)
    last_modified_by = models.CharField(max_length=100, default=None)
    last_modified_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.status_id)


class Media (models.Model):
    media_id = models.AutoField(primary_key=True)
    media_type = models.CharField(max_length=50, default="image")
    file_content = models.FileField(blank=False, null=False)
    file_caption = models.CharField(max_length=100, default=None, blank=True)
    status = models.ForeignKey(
        MediaStatus, on_delete=models.CASCADE, default=None)
    added_by = models.CharField(max_length=100, default=None)
    added_date = models.DateTimeField(default=datetime.now)
    last_modified_by = models.CharField(max_length=100, default=None)
    last_modified_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.media_id)
