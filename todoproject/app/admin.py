from django.contrib import admin
from .models import Task, Blog, Entry, Author
# Register your models here.
admin.site.register(Task)
admin.site.register(Blog)
admin.site.register(Entry)
admin.site.register(Author)
