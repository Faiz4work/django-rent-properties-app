from django.urls import path
from . import views


app_name = "document"

urlpatterns = [
    path('', views.documents, name='documents'),
    path('client/<int:pk>', views.client, name='docclient'),
    path('property/<int:pk>', views.property, name='docprop'),
]