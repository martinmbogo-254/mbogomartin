from django.contrib import admin
from .models import Skill, Profile, Project

# Register your models here.

admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Profile)
