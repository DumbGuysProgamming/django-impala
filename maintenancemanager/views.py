from django.shortcuts import render
from django.http import Http404

from .models import *

def index(request):
    '''Displays a bulleted list of all clients'''
    client_data_list = Client.objects.order_by('-last_name')
    context = {
        'client_data_list': client_data_list
    }
    return render(request, 'maintenancemanager/index.html', context)

def client_information(request, client_id):
    '''this method tries to get client data by id.  If none is found, raises an error'''
    try:
        client_data = Client.objects.get(pk=client_id)
    except Client.DoesNotExist:
        raise Http404("Client does not exist")
    last_name = client_data.last_name
    first_name = client_data.first_name
    return render(request, 'maintenancemanager/client_information.html', {'last_name': last_name, 'first_name': first_name})

