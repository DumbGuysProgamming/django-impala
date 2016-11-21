from django.shortcuts import get_object_or_404, render
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
    client_data = get_object_or_404(Client, pk=client_id)
    return render(request, 'maintenancemanager/client_information.html'
                  , {'client_data': client_data})
