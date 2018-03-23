from django.conf.urls import *# patterns,url
from adminlog.views import *

urlpatterns=[
	url(r'^login-view$',LoginView.as_view()),
	url(r'^login$',login),
]
