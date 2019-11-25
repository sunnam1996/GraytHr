from django.conf.urls import url
from django.urls import path

from .views import *

urlpatterns = [
    url(r'^create/$', salarycreate),
    url(r'^pay/$', salary_slip),
    # url(r'^add-payslip/$', monthly_pay),
    url(r'^payslip/$', payslip),
    url(r'^pf-ytd/$', pf_ytd_statement),
    url(r'^employee/$', employee_select),
    url(r'^employee/(?P<pk>\d+)/$', monthly_pay, name='select-employee'),
    url(r'^salary-revision/$', list_of_salary_employees),
    url(r'^salary-revision/(?P<pk>\d+)/$', salary_revision, name='salary-revision'),
]