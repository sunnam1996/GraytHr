from django.contrib import admin
from .models import *
# Register your models here.

class Admin(admin.ModelAdmin):
    list_display = ['full_name', 'active_flag']
    readonly_fields = ['password']


    class Meta:
        model = Employee


admin.site.register(Employee, Admin)

class BankAdmin(admin.ModelAdmin):
    list_display = ['user', 'bank_name']


    class Meta:
        model = Bankdetails


admin.site.register(Bankdetails, BankAdmin)

class PFAdmin(admin.ModelAdmin):
    list_display = ['uan_number']


    class Meta:
        model = PFdetails


admin.site.register(PFdetails, PFAdmin)

class Qualificationadmin(admin.ModelAdmin):
    list_display = ['user', 'qualification']


    class Meta:
        model = Qualificationdetails
admin.site.register(Qualificationdetails, Qualificationadmin)



class Resignationadmin(admin.ModelAdmin):
    list_display = ['user', 'leaving_reason']


    class Meta:
        model = Resignation

admin.site.register(Resignation, Resignationadmin)


class Careeradmin(admin.ModelAdmin):
    list_display = ['user', 'location']


    class Meta:
        model = Careerinfo

admin.site.register(Careerinfo, Careeradmin)

class EmployeeHistoryadmin(admin.ModelAdmin):
    list_display = ['user', 'company_name']


    class Meta:
        model = EmployeeHistory

admin.site.register(EmployeeHistory, EmployeeHistoryadmin)
