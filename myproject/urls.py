
from django.conf.urls import url
from django.contrib import admin
from dashboard import views as dashboard_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^dashboard/',dashboard_views.maps),
    url(r'^$', dashboard_views.index),
]
