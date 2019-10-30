from django.contrib import admin

from .models import Trip, Passenger, Meetup, TaxiCompany, Log

class MeetupAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude', 'location')

class TripAdmin(admin.ModelAdmin):
    list_display = ('organizer', 'date', 'status', 'latitude', 'longitude')

class PassengerAdmin(admin.ModelAdmin):
    list_display = ('name', 'trip', 'email', 'ip', 'latitude', 'longitude')

class TaxiCompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact')

class LogAdmin(admin.ModelAdmin):
    list_display = ('date', 'activity')

admin.site.register(Trip, TripAdmin)
admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Passenger, PassengerAdmin)
admin.site.register(TaxiCompany, TaxiCompanyAdmin)
admin.site.register(Log, LogAdmin)
