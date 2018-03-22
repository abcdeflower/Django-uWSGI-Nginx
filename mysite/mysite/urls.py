"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from mysite.views import current_datetime,Date_View,Detail_View
from django.conf.urls import include,url

extra_patterns=[
	url(r'(\w)+(?P<pid>(\d)+)/$',Detail_View.as_view(),name='aaaa'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('time/',current_datetime),
    path('class/',Date_View.as_view()),
    path('detail/',include(extra_patterns)),
]
