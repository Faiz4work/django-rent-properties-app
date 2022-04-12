from django.shortcuts import render
from properties.models import Property
import datetime

# Create your views here.
def renewal_page(request):
    renwal_days_limit = 60
    now = datetime.datetime.now()
    two_months_later = now + datetime.timedelta(days=renwal_days_limit)
    props = Property.objects.filter(renewal_date__range=(now,two_months_later))
    context = {
        "props": props,
    }
    return render(request, "renewal/renewal_page.html", context)




