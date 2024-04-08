from django.contrib import admin
from .models import Incident, IncidentStatus, ContactInquiry


class IncidentAdmin(admin.ModelAdmin):
    list_display = ("report_id", "name", "phone", "category", "status")
    list_filter = ("status", "category")
    search_fields = ("name", "phone", "category", "status")


admin.site.register(Incident, IncidentAdmin)


class IncidentStatusAdmin(admin.ModelAdmin):
    list_display = ("status_id", "status_name")


admin.site.register(IncidentStatus, IncidentStatusAdmin)


class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "property_type", "subject")
    list_filter = ("property_type",)
    search_fields = ("name", "email", "phone", "subject")


admin.site.register(ContactInquiry, ContactInquiryAdmin)

admin.site.site_header = "Smart Society Management"
