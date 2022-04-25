from django.contrib import admin
from .models import ClientDoc, PropertyDoc

# Register your models here.


class MyClientDoc(admin.ModelAdmin):
    class Media:   
        css = {
             'all': ('/static/css/admin.css ',)
        }
admin.site.register(ClientDoc,MyClientDoc)


class MyPropertyDoc(admin.ModelAdmin):
    class Media:   
        css = {
             'all': ('/static/css/admin.css ',)
        }
admin.site.register(PropertyDoc, MyPropertyDoc)

