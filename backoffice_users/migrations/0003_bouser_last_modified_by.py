# Generated by Django 2.2.6 on 2019-11-20 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice_users', '0002_auto_20191120_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='bouser',
            name='last_modified_by',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
