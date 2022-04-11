from django.shortcuts import render

# Create your views here.
def renewal_page(request):
    return render(request, "renewal/renewal_page.html")