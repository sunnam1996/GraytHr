from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path

from .views import *

urlpatterns = [
    url(r'^create/$', employee_create),
    url(r'^login/$', employee_login, name='do_login'),
    url(r'^home/$', homepage, name='home'),
    url(r'^changepassword/$', change_password),
    url(r'^list-all-employee/$', all_employee),
    url(r'^bank/(?P<pk>\d+)/$', updatebankdetails, name='bank'),
    url(r'^pf/(?P<pk>\d+)/$', updatepfdetails, name='pf'),
    url(r'^qualify/(?P<pk>\d+)/$', updatequalificationdetails, name='qualification'),
    url(r'^search/$', search_employee),
    url(r'^lead/$', assign_lead),
    url(r'^lead/(?P<pk>\d+)/$',select_employee_lead,name='assign-lead'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^add-bank/$', bankcreate),
    url(r'^add-pf/$', pfdetails),
    url(r'^add-qualification/$', qualificationcreate),
    url(r'^resignation/$', resignationcreate),
    url(r'^careerinfo/$', careerinfocreate),
    url(r'^employeehistory/$', employeehistorycreate),
    url(r'^family/$', familydetailscreate),
    url(r'^info/$', employee_information),

    # url(r'^leave/$', leave_request),

    url(r'^status/$', check_status),
    url(r'status/(?P<pk>\d+)/$', change_status, name='change_status'),
    url(r'^resignation-list/$', resignation_list),
    url(r'resignation-list/(?P<pk>\d+)/$', resignation_apply, name='resignation'),


] 
              # + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

