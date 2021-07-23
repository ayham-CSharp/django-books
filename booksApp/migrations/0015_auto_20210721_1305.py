# Generated by Django 3.2.5 on 2021-07-21 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksApp', '0014_auto_20210721_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='bookEng',
            field=models.TextField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]