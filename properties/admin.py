from django.contrib import admin
from .models import Property, Client

# Register your models here.
class MyProperty(admin.ModelAdmin):
    class Media:   
        css = {
             'all': ('/static/css/admin.css ',)
        }
admin.site.register(Property, MyProperty)      
        
class MyClient(admin.ModelAdmin):
    class Media:   
        css = {
             'all': ('/static/css/admin.css ',)
        }

admin.site.register(Client, MyClient)
