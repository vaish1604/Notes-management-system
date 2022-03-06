from django.contrib import admin
from .models import signup_table
from .models import faculty_signup
# Register your models here.

admin.site.register(signup_table)
admin.site.register(faculty_signup)