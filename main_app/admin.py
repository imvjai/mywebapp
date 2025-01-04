# Register your models here.
from django.contrib import admin
from .models import Project, Blog, Subscriber

admin.site.register(Project)
admin.site.register(Blog)
admin.site.register(Subscriber)
