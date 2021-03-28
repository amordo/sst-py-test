from django.conf.urls import url
from . import views

urlpatterns = [
    url('^', views.manage_entities, name='manage_entities'),
]
