# Generated by Django 3.2.5 on 2021-07-15 11:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booksApp', '0003_createbook_publisher'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='createBook',
            new_name='Book',
        ),
    ]
