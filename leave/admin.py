from django.contrib import admin
from .models import *
# Register your models here.


class Admin(admin.ModelAdmin):
    list_display = ['type', 'active_flag']

    class Meta:
        model = Leavetype


admin.site.register(Leavetype, Admin)


class LeaveApplyAdmin(admin.ModelAdmin):
    list_display = ['reason', 'status', 'active_flag']

    class Meta:
        model = Leaveapply

admin.site.register(Leaveapply, LeaveApplyAdmin)


class Assignleaveadmin(admin.ModelAdmin):
    list_display = ['leavetype', 'balance', 'assign_leave_to']

    class Meta:
        model = Leavebalance

admin.site.register(Leavebalance, Assignleaveadmin)
