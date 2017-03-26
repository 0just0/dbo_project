from django.conf.urls import include, url
from django.contrib import admin
from banks import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^banks/', include('banks.urls', namespace='banks', app_name='banks')),
]
