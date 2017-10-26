"""cmdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from user.views import login,database,add_user,user_info,home,user_detail,add_user

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login', add_user),
    url(r'^database', database),
    url(r'^user_info', user_info),
    url(r'^home', home),
    url(r'^user-detail-(?P<uid>\d+)', user_detail),
    url(r'^add-user', add_user),
]
