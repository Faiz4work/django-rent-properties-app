app_name = "properties"

from django.urls import path
from . import views

urlpatterns = [
    path('', views.properties, name='prop'),
    path('addproperty/', views.add_prop, name='add_prop'),
    path('<int:pk>/', views.details, name='details'),
    path('<str:pk>/delete/', views.delete_prop, name='delete_prop'),
    
    # clients urls
    path('clients/', views.clients, name='clients'),
]