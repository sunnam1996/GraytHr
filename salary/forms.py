from django.forms import DateInput

from .models import *
from django import forms



class SalaryDisplayForm(forms.ModelForm):



    class Meta:
        model = Salarydetails
        fields = ['emp_id', 'cost_to_company']



class SalaryCreateForm(forms.ModelForm):

    class Meta:
        model = Salarydetails
        exclude = ['active_flag', 'created_on', 'modified_on']



class MonthlyslipForm(forms.ModelForm):

    class Meta:
        model = MonthlySlip
        exclude = [ 'active_flag', 'created_on', 'modified_on']





class MonthlyslipDisplayForm(forms.ModelForm):

    class Meta:
        model = MonthlySlip
        # exclude = [ 'basic_pay', 'hra', 'bonus', 'special_allowance', 'pf', 'emp_id', 'earning', 'deduction', 'total_income', 'active_flag', 'created_on', 'modified_on']
        fields = ['year', 'month']



class SalaryRevisionForm(forms.ModelForm):
    per = forms.CharField()


    class Meta:
        model = Salarydetails
        fields = '__all__'


class SalaryRevisionDisplayForm(forms.ModelForm):
    per = forms.CharField()

    class Meta:
        model = Salarydetails
        fields = ['cost_to_company', 'per']