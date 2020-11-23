from django.db import models
from datetime import datetime
from media_management.models import Media


class BlogStatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=100)
    added_by = models.CharField(max_length=100, default=None)
    added_date = models.DateTimeField(default=datetime.now)
    last_modified_by = models.CharField(max_length=100, default=None)
    last_modified_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.status_id)


class ParagraphStatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=100)
    added_by = models.CharField(max_length=100, default=None)
    added_date = models.DateTimeField(default=datetime.now)
    last_modified_by = models.CharField(max_length=100, default=None)
    last_modified_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.status_id)


class Blog(models.Model):
    blog_id = models.AutoField(primary_key=True)
    blog_title = models.CharField(max_length=100)
    blog_status = models.ForeignKey(
        BlogStatus, on_delete=models.CASCADE, default=None)
    added_by = models.CharField(max_length=100, default=None)
    added_date = models.DateTimeField(default=datetime.now)
    last_modified_by = models.CharField(max_length=100, default=None)
    last_modified_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.blog_id)


class Paragraph(models.Model):
    paragraph_id = models.AutoField(primary_key=True)
    paragraph_body = models.TextField(default=None, blank=True)
    status = models.ForeignKey(
        ParagraphStatus, on_delete=models.CASCADE, default=None)
    added_by = models.CharField(max_length=100, default=None)
    added_date = models.DateTimeField(default=datetime.now)
    last_modified_by = models.CharField(max_length=100, default=None)
    last_modified_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.paragraph_id)


class BlogToParagraphMappingStatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=100, default="not defined")
    added_by = models.CharField(max_length=100, default=None)
    added_date = models.DateTimeField(default=datetime.now)
    last_modified_by = models.CharField(max_length=100, default=None)
    last_modified_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.status_id)


class BlogToParagraphMapping(models.Model):
    map_id = models.AutoField(primary_key=True)
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE, default=None)
    paragraph_id = models.ForeignKey(
        Paragraph, on_delete=models.CASCADE, default=None)
    status = models.ForeignKey(
        BlogToParagraphMappingStatus, on_delete=models.CASCADE, default=None)
    added_by = models.CharField(max_length=100, default=None)
    added_date = models.DateTimeField(default=datetime.now)
    last_modified_by = models.CharField(max_length=100, default=None)
    last_modified_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.map_id)


class MetaTagStatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=100, default="not defined")
    added_by = models.CharField(max_length=100, default=None)
    added_date = models.DateTimeField(default=datetime.now)
    last_modified_by = models.CharField(max_length=100, default=None)
    last_modified_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.status_id)


class MetaTagType(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=100, default="not defined")
    type_name_value = models.CharField(max_length=100, default="not defined")
    added_by = models.CharField(max_length=100, default=None)
    added_date = models.DateTimeField(default=datetime.now)
    last_modified_by = models.CharField(max_length=100, default=None)
    last_modified_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.type_id)


class MetaTag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    type_id = models.ForeignKey(
        MetaTagType, on_delete=models.CASCADE, default=None)
    content = models.CharField(max_length=100, default="not defined")
    status = models.ForeignKey(
        MetaTagStatus, on_delete=models.CASCADE, default=None)
    added_by = models.CharField(max_length=100, default=None)
    added_date = models.DateTimeField(default=datetime.now)
    last_modified_by = models.CharField(max_length=100, default=None)
    last_modified_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.tag_id)


class BlogToMetaTagMappingStatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=100, default="not defined")
    added_by = models.CharField(max_length=100, default=None)
    added_date = models.DateTimeField(default=datetime.now)
    last_modified_by = models.CharField(max_length=100, default=None)
    last_modified_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.status_id)


class BlogToMetaTagMapping(models.Model):
    blog_to_meta_tag_map_id = models.AutoField(primary_key=True)
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE, default=None)
    tag_id = models.ForeignKey(MetaTag, on_delete=models.CASCADE, default=None)
    status = models.ForeignKey(
        BlogToMetaTagMappingStatus, on_delete=models.CASCADE, default=None)
    added_by = models.CharField(max_length=100, default=None)
    added_date = models.DateTimeField(default=datetime.now)
    last_modified_by = models.CharField(max_length=100, default=None)
    last_modified_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.blog_to_meta_tag_map_id)


class ParagraphToMediaMappingStatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=100, default="not defined")
    added_by = models.CharField(max_length=100, default=None)
    added_date = models.DateTimeField(default=datetime.now)
    last_modified_by = models.CharField(max_length=100, default=None)
    last_modified_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.status_id)


class ParagraphToMediaMapping(models.Model):
    paragraph_to_media_map_id = models.AutoField(primary_key=True)
    paragraph_id = models.ForeignKey(
        Paragraph, on_delete=models.CASCADE, default=None)
    media_id = models.ForeignKey(Media, on_delete=models.CASCADE, default=None)
    status = models.ForeignKey(
        ParagraphToMediaMappingStatus, on_delete=models.CASCADE, default=None)
    added_by = models.CharField(max_length=100, default=None)
    added_date = models.DateTimeField(default=datetime.now)
    last_modified_by = models.CharField(max_length=100, default=None)
    last_modified_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.paragraph_to_media_map_id)
