# Generated by Django 3.2.5 on 2021-07-17 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksApp', '0007_alter_book_bookimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='bookImage',
            field=models.ImageField(upload_to='book/'),
        ),
    ]
