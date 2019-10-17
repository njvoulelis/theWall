from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.loginReg),
    url(r'^process$', views.process),
    url(r'^login$', views.login),
    url(r'^success$', views.success),
    url(r'^logout$', views.logout),
]