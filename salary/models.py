from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
from employee.models import *

def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


month_type = (('Jan', 'January'), ('Feb', 'February'), ('Mar', 'March '),
              ('Apr', 'April'), ('May', 'May'), ('Jun', 'June'), ('Jul', 'July'),
              ('Aug', 'August'), ('Sep', 'September'), ('Oct', 'October '), ('Nov', 'November'), ('Dec', 'December'))

class Salarydetails(models.Model):
    user = models.ForeignKey(Employee, on_delete=models.CASCADE)
    emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='emp_id')
    cost_to_company = models.DecimalField(max_digits=12, decimal_places=2)
    basic_pay = models.DecimalField(max_digits=12, decimal_places=2)
    hra = models.DecimalField(max_digits=12, decimal_places=2)
    bonus = models.DecimalField(max_digits=12, decimal_places=2)
    special_allowance = models.DecimalField(max_digits=12, decimal_places=2)
    pf = models.DecimalField(max_digits=12, decimal_places=2)
    esi = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)

    monthly_basic_pay = models.DecimalField(max_digits=12, decimal_places=2)
    monthly_hra =models.DecimalField(max_digits=12, decimal_places=2)
    monthly_bonus = models.DecimalField(max_digits=12, decimal_places=2)
    monthly_special_allowance = models.DecimalField(max_digits=12, decimal_places=2)
    monthly_pf = models.DecimalField(max_digits=12, decimal_places=2)
    monthly_esi = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    monthly_salary = models.DecimalField(max_digits=12, decimal_places=2)
    active_flag = models.BooleanField(('active'), default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)


class MonthlySlip(models.Model):
    year = models.IntegerField(validators=[MinValueValidator(1990), max_value_current_year])
    month = models.CharField(max_length=30, choices=month_type)
    emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='empl_id')
    basic_pay = models.DecimalField(max_digits=12, decimal_places=2)
    hra = models.DecimalField(max_digits=12, decimal_places=2)
    bonus = models.DecimalField(max_digits=12, decimal_places=2)
    special_allowance = models.DecimalField(max_digits=12, decimal_places=2)
    pf = models.DecimalField(max_digits=12, decimal_places=2)
    esi = models.DecimalField(max_digits=12, decimal_places=2)
    earning = models.DecimalField(max_digits=12, decimal_places=2)
    deduction = models.DecimalField(max_digits=12, decimal_places=2)
    total_income = models.DecimalField(max_digits=12, decimal_places=2)
    active_flag = models.BooleanField(('active'), default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

