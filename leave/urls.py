from django.conf.urls import url
from django.urls import path
from .views import *


urlpatterns=[
    url(r'^leavetype/', leavetypecreate),
    url(r'^leaveapply/', leaveapplycreate, name='leaveapply'),
    path('leavecancel/<int:pk>/', leavecancel, name='leave_cancel'),
    url('leavecancel_list/', leavecancel_list, name='leavecancel_list'),
    url(r'^leavetrack/$', leavetrack),
    url(r'^assign_leave/$', assign_leavebalance),
    # url(r'^update_leave/$', update_leavebalance, name='leave'),
    url(r'^update_leave/(?P<pk>\d+)/$', update_leavebalance, name='leave'),
    url(r'leave_request/$', leave_request_list),
    url(r'leave_request/(?P<pk>\d+)/$', leave_status),
    path('pending_requests/', pending_requests, name='pending_requests'),
    path('leave_status/<int:pk>/<int:status>/', leave_status, name='leave_status')
]



