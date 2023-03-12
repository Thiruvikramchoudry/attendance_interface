from django.contrib import admin
from .models import details,attendence_area,absenteeism_count
# Register your models here.


admin.site.register(details)
admin.site.register(attendence_area)
admin.site.register(absenteeism_count)
