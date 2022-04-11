from django.shortcuts import render
from properties.models import *
from document.models import ClientDoc, PropertyDoc


# Create your views here.

def documents(request):
    clients = Client.objects.all()
    properties = Property.objects.all()
    context = {
        "clients": clients,
        "properties": properties,
    }
    return render(request, "document/doc.html", context)


def client(request, pk):
    docs = ClientDoc.objects.filter(client_id=pk).all()
    context = {
        "docs": docs,
    }
    return render(request, "document/doc_files.html", context)


def property(request, pk):
    props = PropertyDoc.objects.filter(property_id=pk).all()
    context = {
        "docs": props,
    }
    return render(request, "document/doc_files.html", context)



