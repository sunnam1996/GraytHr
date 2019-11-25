from django import forms
from django.core.exceptions import ValidationError
from .models import *


# class AddUserForm(forms.ModelForm):
#
#     class Meta:
#         model = CustomUser
#         fields = ('username', 'Employee_first_name', 'Middle_name', 'Employee_last_name', 'email', 'ph_no', 'emp_type')
#
#
# class EditUserForm(forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = ('Employee_first_name', 'Middle_name', 'Employee_last_name', 'email', 'ph_no', 'emp_type', 'user_status')
#
