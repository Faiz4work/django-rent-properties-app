app_name = "renewal"

from django.urls import path
from . import views

urlpatterns = [
    path('', views.renewal_page, name='renewal_page'),
]