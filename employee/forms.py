from .models import *
from django import forms



class EmployeeDisplayform(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ['full_name', 'email', 'date_of_birth', 'mobile', 'password']



class EmployeeCreateform(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ['full_name', 'email', 'date_of_birth', 'mobile', 'password', 'date_of_joining', 'blood_group', 'marital_status', 'pan_card']


class Employeeloginform(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ['employee_id', 'password']


class Changepasswordform(forms.ModelForm):
    new_password = forms.CharField(max_length=40)
    re_enter_new_password = forms.CharField(max_length=40)



    class Meta:
        model = Employee
        fields = ['password', 'new_password', 're_enter_new_password']

class Assignleadform(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ['full_name', 'reporting_lead']


class Bankdetailsform(forms.ModelForm):

    class Meta:
        model = Bankdetails
        fields = ['bank_name', 'ifsc_code', 'bank_account_holder_name', 'bank_account_number', 'branch_name', 'account_type', 'payment_type', 'user']

class BankDisplayform(forms.ModelForm):

    class Meta:
        model = Bankdetails
        fields = ['bank_name', 'ifsc_code', 'bank_account_holder_name', 'bank_account_number', 'branch_name', 'account_type', 'payment_type']


class PFdisplayform(forms.ModelForm):

    class Meta:
        model = PFdetails
        fields = ['pf_join_date', 'pf_scheme', 'uan_number', 'pf_number', 'esi_number', 'family_pf_number']



class PFdetailsform(forms.ModelForm):

    class Meta:
        model = PFdetails
        fields = ['pf_join_date', 'pf_scheme', 'uan_number', 'pf_number', 'esi_number', 'family_pf_number', 'user']


class Qualificationcreateform(forms.ModelForm):

    class Meta:
        model = Qualificationdetails
        fields = ['qualification', 'from_date', 'to_date', 'institute', 'grade', 'qualification_area', 'user']


class QualificationDisplayform(forms.ModelForm):

    class Meta:
        model = Qualificationdetails
        fields = ['qualification', 'from_date', 'to_date', 'institute', 'grade', 'qualification_area']


class ResignationDisplayForm(forms.ModelForm):

    class Meta:
        model = Resignation
        fields = ['leaving_reason']


class ResignationCreateForm(forms.ModelForm):

    class Meta:
        model = Resignation
        exclude = ['leaving_date', 'final_settlement_date', 'date_of_relieve', 'remarks']


class CareerinfoDisplayform(forms.ModelForm):

    class Meta:
        model = Careerinfo
        exclude = ['user']


class CareerinfoCreateform(forms.ModelForm):

    class Meta:
        model = Careerinfo
        fields = ['location', 'designation', 'user']


class EmployeeHistoryDisplayform(forms.ModelForm):

    class Meta:
        model = EmployeeHistory
        exclude = ['user', 'active_flag']


class EmployeeHistoryCreateform(forms.ModelForm):


    class Meta:
        model = EmployeeHistory
        fields = '__all__'


class FamilydetailsDisplayForm(forms.ModelForm):

    class Meta:
        model = Familydetails
        exclude = ['user', 'active_flag']


class FamilydetailsCreateForm(forms.ModelForm):


    class Meta:
        model = Familydetails
        fields = '__all__'


class CheckstatusForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ['full_name', 'employee_id', 'date_of_joining', 'confirmation_date', 'emp_status']