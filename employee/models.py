from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models

role_type = (('dev', 'Developers'),
('lead', 'Team Lead'),
('manager', 'Project Manager'),
('hr', 'HR'),
('su', 'Super User')
)

gender_type = (('m', 'Male'), ('f', 'Female'))


def past(date):
    if date > date.today():
        raise ValidationError("Date cannot be greater")


marital = (('s', 'Single'), ('m', 'Married'))

emp_type = (('pp', 'Probation Period'), ('cn', 'Confirmed'))

blood_group_type = (('A+', 'A +ve'), ('A-', 'A -ve'), ('B+', 'B +ve'), ('B-', 'B -ve'), ('O+', 'O +ve'), ('O-', 'O -ve'), ('AB+', 'AB +ve'), ('AB+', 'AB -ve'))


# Create your models here.


class Employee(models.Model):
    full_name = models.CharField(max_length=40)
    date_of_birth = models.DateField(validators=[past])
    email = models.EmailField(max_length=70, unique=True)
    employee_id = models.CharField(max_length=20, unique=True)
    mobile = models.CharField(max_length=10, validators=[RegexValidator(regex="^[0-9]{10}$", message='Length has to be ten digits and only numbers are allowed', code='nomatch')])
    role = models.CharField(max_length=32, choices=role_type, default='dev')
    reporting_lead = models.CharField(max_length=20)
    password = models.CharField(max_length=40)
    date_of_joining = models.DateField()
    confirmation_date = models.DateField(null=True, blank=True)
    # profile_image = models.ImageField(upload_to='files', null=True)
    emp_status = models.CharField(max_length=20, choices=emp_type, default='pp')
    blood_group = models.CharField(max_length=30, choices=blood_group_type,null=True, blank=True)
    marital_status = models.CharField(max_length=20,null=True, blank=True, choices=marital)
    pan_card = models.CharField(max_length=10, null=True, blank=True, validators=[RegexValidator(regex='^.{10}$', message='Length has to be 10', code='nomatch')])
    active_flag = models.BooleanField(('active'), default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


    # def __str__(self):
    #     return  "AIPL/" +  str(self.id)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password


    def check_password(self, raw_password):
        def setter(raw_password):
            self.set_password(raw_password)
            self._password = None
            self.save(update_fields=["password"])
        return check_password(raw_password, self.password, setter)


class Bankdetails(models.Model):
    user= models.ForeignKey(Employee, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=40)
    ifsc_code = models.CharField(max_length=11, validators=[RegexValidator(regex='^.{11}$', message='IFSC code should be 11 digits', code='nomatch')])
    bank_account_holder_name = models.CharField(max_length=32)
    bank_account_number = models.CharField(max_length=20)
    branch_name = models.CharField(max_length=32)
    account_type = models.CharField(max_length=20)
    payment_type = models.CharField(max_length=20)
    active_flag = models.BooleanField(('active'), default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.bank_account_holder_name



class PFdetails(models.Model):
    user = models.ForeignKey(Employee, on_delete=models.CASCADE)
    pf_join_date = models.DateField()
    pf_scheme = models.CharField(max_length=30)
    uan_number = models.CharField(max_length=12, validators=[RegexValidator(regex='^.{12}$', message='UAN number should be 12 digits', code='nomatch')])
    pf_number = models.CharField(max_length=32)
    esi_number = models.CharField(max_length=20)
    family_pf_number = models.CharField(max_length=32)
    active_flag = models.BooleanField(('active'), default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.uan_number



class Qualificationdetails(models.Model):
    user = models.ForeignKey(Employee, on_delete=models.CASCADE)
    qualification= models.CharField(max_length=60)
    from_date = models.DateField()
    to_date = models.DateField()
    institute = models.CharField(max_length=120)
    grade = models.CharField(max_length=40)
    qualification_area = models.CharField(max_length=40)
    active_flag = models.BooleanField(('active'), default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.qualification



class Resignation(models.Model):
    user = models.ForeignKey(Employee, on_delete=models.CASCADE)
    submitted_on = models.DateField()
    leaving_reason = models.CharField(max_length=120)
    leaving_date = models.DateField(null=True, blank=True)
    final_settlement_date = models.DateField(null=True,blank=True)
    date_of_relieve = models.DateField(null=True,blank=True)
    remarks = models.CharField(max_length=120, null=True, blank=True)
    active_flag = models.BooleanField(('active'), default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.leaving_reason


class Careerinfo(models.Model):
    user = models.ForeignKey(Employee, on_delete=models.CASCADE)
    location = models.CharField(max_length=40)
    designation = models.CharField(max_length=40)
    active_flag = models.BooleanField(('active'), default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.location


class EmployeeHistory(models.Model):
    user = models.ForeignKey(Employee, on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField()
    designation = models.CharField(max_length=40)
    company_name = models.CharField(max_length=40)
    company_address = models.CharField(max_length=120)
    active_flag = models.BooleanField(('active'), default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user


# class Leave(models.Model):
#     user = models.ForeignKey(Employee, on_delete=models.CASCADE)
#     From = models.DateField(auto_now=False, auto_now_add=False)
#     To = models.DateField(auto_now=False, auto_now_add=False)
#     LeaveType = models.CharField(max_length=10, choices=[('Casual', 'Casual'),
#                                                          ('Sick', 'Sick'),
#                                                          ('Comp off', 'Comp off')])
#     Fromsession = models.CharField(max_length=50, choices=[('Session1', 'Session1'),
#                                                            ('Session2', 'Session2'),
#                                                            ], default='Session1')
#     Tosession = models.CharField(max_length=50, choices=[('Session1', 'Session1'),
#                                                          ('Session2', 'Session2'),
#                                                          ], default='Session1')
#     Days = models.CharField(max_length=10, default=' ')
#     Balance_days = models.CharField(max_length=10, default=' ')
#     ApplyTo = models.EmailField(max_length=70, choices=[('Manager', 'Manager'),
#                                                         ('Hr', 'Hr'),
#                                                         ('Admin', 'Admin')], default='')
#     CcTo = models.EmailField(default='')
#     Contact = models.CharField(max_length=10, default='')
#     Reason = models.TextField(max_length=500)
#     Status = models.BooleanField(default=None, null=True)
#     Attachment = models.FileField(upload_to='media/', default='')
        return self.designation


class Familydetails(models.Model):
    user = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    relation = models.CharField(max_length=40)
    date_of_birth = models.DateField()
    blood_group = models.CharField(max_length=30, choices=blood_group_type,null=True, blank=True)
    gender = models.CharField(max_length=20, choices=gender_type)
    nationality = models.CharField(max_length=30)
    profession=models.CharField(max_length=40)
    active_flag = models.BooleanField(('active'), default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.relation

