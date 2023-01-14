from django.contrib import admin
from .models import State,City,Property
# Register your models here.

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['id','state']
    

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id','city','state']

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['id','name','city','state']
