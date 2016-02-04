"""pos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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

from core import views

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

from pos.core.views.auth import LogoutView

urlpatterns = patterns(
    'django.contrib.auth.views',
    url(
        r'^login/$', 'login', name='login'),
    url(
        r'^logout/$', LogoutView.as_view(), {'next_page': '/'}, name='logout'),
    url(
        r'^password/reset/$', 'password_reset',
        {'from_email': settings.SUPPORT_EMAIL},
        name='password-reset'),
    url(
        r'^password/reset/done/$', 'password_reset_done',
        name='password_reset_done'),
    url(
        (
            r'^password/(?P<uidb64>[0-9A-Za-z]{1,13})-'
            r'(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$'
        ),
        'password_reset_confirm',
        name='set-password'),
    url(
        (
            r'^reset/(?P<uidb64>[0-9A-Za-z]{1,13})-'
            r'(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$'
        ),
        'password_reset_confirm',
        name='password_reset_confirm'),

    url(r'^reset/done/$',
        'password_reset_complete',
        name='password_reset_complete'),

    url(r'social/',
        include('social.apps.django_app.urls', namespace='social')),
)



urlpatterns += [
    url(r'^admin/', admin.site.urls),
#    url(r'^', views.PosView.as_view(), name='pos'),
]
