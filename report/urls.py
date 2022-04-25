from django.urls import path
from . import views

app_name = "report"


urlpatterns = [
    path('', views.report, name='report_page'),
    path('profit/', views.profit, name='profit'),
    path('expenses/', views.expenses, name='expenses'),
    path('add_expense/', views.add_expense, name='add_expense'),
    path('expense_details/<int:pk>', views.expense_details, name='expense_details'),
]