from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import TrackInfo, RequestMessage


@admin.register(TrackInfo)
class TrackInfoAdmin(ModelAdmin):
    list_display = [
        "shipment_number",
        "shipment_id_create_time",
        "shipment_org_name",
        "country_code",
        "shop_name",
        "shipment_departure_time",
        "shipment_enter_uzb",
        "shipment_process_local",
        "shipment_received_time",
    ]
    list_display_links = ["shipment_number"]
    list_filter = [
        "country_code",
        "shipment_id_create_time",
        "shipment_received_time",
    ]
    list_editable = [
        "country_code",
        "shipment_departure_time",
        "shipment_enter_uzb",
        "shipment_process_local",
        "shipment_received_time",
    ]
    exclude = ["correlation_id"]
    # readonly_fields = ["correlation_id"]


@admin.register(RequestMessage)
class RequestMessageAdmin(ModelAdmin):
    list_display = ["first_name", "email", "subject", "created_at"]
    list_filter = ["created_at"]
