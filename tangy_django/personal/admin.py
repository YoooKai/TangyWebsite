from django.contrib import admin
from .models import About, Commissions, FAQ, Contact

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(Commissions)
class CommissionsAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'slots_left')
    search_fields = ('title',)
    list_filter = ('slots_left',)

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question',)
    search_fields = ('question',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name',  'email')
    search_fields = ('name', 'email')
    readonly_fields = ('name', 'email', 'message')
