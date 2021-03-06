# Generated by Django 3.2.5 on 2021-07-19 08:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booksApp', '0009_book_craeted_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='comments',
            fields=[
                ('commentId', models.AutoField(primary_key=True, serialize=False)),
                ('bookNotes', models.TextField(max_length=200)),
                ('craeted_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='booksApp.book')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentsUser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
