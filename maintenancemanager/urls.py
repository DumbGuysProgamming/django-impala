from django.conf.urls import url

from . import views

urlpatterns = [
    #index
    url(r'^$', views.index, name='index'),
    #vehicle
    # url(r'^(?P<vehicle_id>[0-9]+)/vehicle/$', views.vehicle_information, name='vehicle'),
    #client
    url(r'^(?P<client_id>[0-9]+)/client/$', views.client_information, name='client'),
    #service
    # url(r'^(?P<service_id>[0-9]+)/service/$', views.service_information, name='service'),
]
