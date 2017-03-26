from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^search/fl$', views.search_fl, name='search'),
    url(r'^search/ul$', views.search_ul, name='search_ul'),
]
