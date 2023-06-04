from django.contrib import admin
from .models import Peopleinfo
class AdminPeopleinfo(admin.ModelAdmin):
    list_display= ['name','preg','glu','bp','insulin','height','weight','dpf','age','gender']
# Register your models here.
admin.site.register(Peopleinfo,AdminPeopleinfo)