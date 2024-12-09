from django.contrib import admin
from .models import Schoolclass, Finance,Invoice
from core.models import Contact

# Register your models here.
admin.site.register(Schoolclass)
admin.site.register(Finance)
admin.site.register(Invoice)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'message')