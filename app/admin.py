from django.contrib import admin
from .models import *

# Register your models here.
class studentadmin(admin.ModelAdmin):
    list_display=['name','email','phoneno']
admin.site.register(student,studentadmin)
admin.site.register(savefile)

