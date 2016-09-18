"""code2do URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^checkvalidity$', views.checkvalidity, name='checkvalidity'),
    url(r'^profile$', views.profile, name="profile"),
    url(r'^register$', views.register, name='register'),
    url(r'^logout$', views.logout, name="logout"),
    url(r'^add_new_user$', views.add_new_user, name='add_new_user'),
    url(r'^addproblem$', views.addproblem, name='addproblem'),
    url(r'^profile/codechef$', views.codechef, name="codechef"),
    url(r'^profile/hackerearth$', views.hackerearth, name="hackerearth"),
    url(r'^profile/spoj$', views.spoj, name="spoj"),
    url(r'^profile/codeforces$', views.codeforces, name="codeforces"),
    url(r'^profile/hackerrank$', views.hackerrank, name="hackerrank"),
    url(r'^marksolved$', views.marksolved, name='marksolved'),
    url(r'^admin/', admin.site.urls),
]
