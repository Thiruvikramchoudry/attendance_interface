from django.contrib import admin
from .models import employee_details,supervisor_detail,supervisor_assign,project,employee_assign
# Register your models here.


admin.site.register(employee_details)
admin.site.register(supervisor_assign)
admin.site.register(supervisor_detail)
admin.site.register(project)
admin.site.register(employee_assign)


