from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Property, Client
# Create your views here.

def properties(request):
    props = Property.objects.all()
    context = {'props': props}
    return render(request, 'properties/prop.html', context)

def add_prop(request):
    if request.method=='POST':
        address = request.POST.get('address')
        client = request.POST.get('client')
        price = request.POST.get('price')
        documents = request.POST.get('documents')
        history = request.POST.get('history')
        rented_since = request.POST.get('rented_since')
        rented_to = request.POST.get('rented_to')
        renewal_date = request.POST.get('renewal_date')
        print(request.POST)
    return render(request, "properties/add_prop.html")

def details(request, pk):
    obj = Property.objects.filter(pk=pk).first()
    context = {
        "obj": obj,
    }
    return render(request, 'properties/prop_details.html', context)

def delete_prop(request, pk):
    obj = Property.objects.filter(pk=pk).first()
    obj.delete()
    return HttpResponseRedirect(reverse('properties:prop'))


# Clients views
def clients(request):
    cl = Client.objects.all()
    context = {
        'clients': cl,
    }
    return render(request, "properties/clients.html", context)