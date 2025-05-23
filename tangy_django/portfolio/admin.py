
from django.contrib import admin
from .models import PortfolioEntry

@admin.register(PortfolioEntry)
class PortfolioEntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category',)
    ordering = ('-created_at',)
