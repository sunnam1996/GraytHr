"""appy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

from employee.views import employee_login

urlpatterns = [
    path('admin/', admin.site.urls),
    url('employee/', include('employee.urls')),

    # path('leave/', include('leave.urls')),


    # path('accounts/', include('django.contrib.auth.urls')),
    # path('home/',views.homepage),
    # path('staff/',views.staff),
    # path('superuser/',views.superuser)
    path('leave/', include('leave.urls')),
    path('salary/', include('salary.urls')),
    path('login/', employee_login, name='do_login'),
    # url(r'^signup/', TemplateView.as_view(template_name='signup.html')),
    # url(r'^login/', TemplateView.as_view(template_name='login.html')),
    # url('leave/', include('employee.urls')),
    # url(r'^', TemplateView.as_view(template_name='homepage.html'))
    path('home/', include('myapp.urls') ),
    path('', include('django.contrib.auth.urls')),
    path('', include('fullcalender.urls')),
    path('home', TemplateView.as_view(template_name='home.html'), name='home'),
    path('leave',TemplateView.as_view(template_name='home.html'), name='leave'),

]

if settings.DEBUG:
    # urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)