from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^wall$', views.viewWall),
    url(r'^postMessage$', views.postMessage),
    url(r'^postComment$', views.postComment),
    url(r'^deleteComment$', views.deleteComment),
]