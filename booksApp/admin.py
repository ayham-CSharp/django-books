from django.contrib import admin

# Register your models here.
from .models import book,comment

admin.site.register(book)
admin.site.register(comment)