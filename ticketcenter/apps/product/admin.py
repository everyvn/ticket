from django.contrib import admin
from .models import Category, Show, Tag

# Register your models here.
admin.site.register(Category)
admin.site.register(Show)
admin.site.register(Tag)