from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# Create your models here.


# class CustomUser(models.Model):
#     name = models.CharField(max_length=300)
#     Employee_first_name = models.CharField(max_length=100, default='')
#     Middle_name = models.CharField(max_length=100, default='', blank=True)
#     Employee_last_name = models.CharField(max_length=100, default='')
#     email = models.EmailField()
#     ph_no = models.CharField(max_length=10)
#     emp_type = models.CharField(max_length=10, choices=[('Manager', 'Manager'),
#                                                         ('Hr','Hr'),
#                                             ('Employee', 'Employee'),
#                                             ])
#     user_status = models.CharField(max_length=10, default='Active', choices=[('Active', 'Active'),
#                                                             ('Inactive', 'Inactive')])

# class Mapping(models.Model):
#     Employee = models.ManyToManyField(CustomUser)
#     Manager = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='manager')
    # Hr  = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='user_as_hr')

class LeaveRequest(models.Model):

    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    From = models.DateField(auto_now=False, auto_now_add=False)
    To = models.DateField(auto_now=False, auto_now_add=False)
    LeaveType = models.CharField(max_length=10, choices=[('Casual', 'Casual'),
                                                            ('Sick', 'Sick'),
                                                            ('Comp off', 'Comp off')])
    Fromsession= models.CharField(max_length=50, choices=[('Session1', 'Session1'),
                                                         ('Session2', 'Session2'),
                                                         ],default='Session1')
    Tosession = models.CharField(max_length=50, choices=[('Session1', 'Session1'),
                                                           ('Session2', 'Session2'),
                                                           ], default='Session1')
    Days = models.CharField(max_length=10,default=' ')
    Balance_days = models.CharField(max_length=10,default=' ')
    ApplyTo = models.EmailField(max_length=70,choices=[('Manager','Manager'),
                                         ('Hr','Hr'),
                                         ('Admin','Admin')],default='')
    CcTo = models.EmailField(default='')
    Contact = models.CharField(max_length=10,default='')
    Reason = models.TextField(max_length=500)
    Status = models.BooleanField(default=None, null=True)
    Attachment = models.FileField(upload_to='media/',default='')
