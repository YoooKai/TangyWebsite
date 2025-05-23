from django.contrib import admin
from .models import UpcomingEvent

@admin.register(UpcomingEvent)
class UpcomingEventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'location')
    list_filter = ('start_date',)
