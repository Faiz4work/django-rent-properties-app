from django.shortcuts import render

# Create your views here.

def report(request):
    return render(request, "report/report_page.html")

def profit(request):
    return render(request, "report/profit.html")

def expenses(request):
    return render(request, "report/expense.html")