from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import *

def index(request):
    client_data_list = Client.objects.order_by('-last_name')
    template = loader.get_template('maintenancemanager/index.html')
    context = {
        'client_data_list': client_data_list
    }
    return HttpResponse(template.render(context, request))

def client_information(request, client_id):
    client_data = Client.objects.get(pk=client_id)
    client_name = '{}, {}'.format(client_data.last_name, client_data.first_name)
    return HttpResponse("You're looking at information for client: %s." % client_name)

def service_information(request, service_id):
    return HttpResponse("You're looking at information for service: %s." % service_id)

def vehicle_information(request, vehicle_id):
    return HttpResponse("You're looking at information for vehicle: %s." % vehicle_id)
