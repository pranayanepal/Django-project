from django.contrib import admin
from .models import Employes,Department,Role
# Register your models here.

admin.site.register(Employes)
admin.site.register(Department)
admin.site.register(Role)