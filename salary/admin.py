from django.contrib import admin
from .models import *




# Register your models here.
class Admin(admin.ModelAdmin):
    list_display = ['emp_id', 'active_flag']
    # readonly_fields = ['password']


    class Meta:
        model = Salarydetails


admin.site.register(Salarydetails, Admin)
admin.site.register(MonthlySlip)