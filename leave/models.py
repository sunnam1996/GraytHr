from django.db import models
from employee.models import Employee
from datetime import date

# Create your models here.

session_type = (('1', 'session 1'), ('2', 'session 2'))
status_type = ((1, 'Accept'), (0, 'Reject'))


class Leavetype(models.Model):
    type = models.CharField(max_length=40)
    active_flag = models.BooleanField(('active'), default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.type

class Leaveapply(models.Model):
    leavetype = models.ForeignKey(Leavetype, on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField()
    from_session = models.CharField(max_length=40, choices=session_type)
    to_session = models.CharField(max_length=40, choices=session_type)
    days = models.IntegerField(null=True)
    apply_to = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='lead')
    reason = models.CharField(max_length=40)
    cc_to = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='management')
    status= models.BooleanField(choices=status_type,null=True)
    by = models.ForeignKey(Employee, on_delete=models.CASCADE)
    active_flag = models.BooleanField(('active'), default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.reason

    # def days_calc(self):
    #     self.days = self.to_date - self.from_date
    #     return self.days

class Leavebalance(models.Model):
    balance = models.IntegerField()
    leavetype = models.ForeignKey(Leavetype, on_delete=models.CASCADE)
    assign_leave_to = models.ForeignKey(Employee, on_delete=models.CASCADE)
