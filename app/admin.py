from django.contrib import admin

from .models import TrackInfo


@admin.register(TrackInfo)
class TrackInfoAdmin(admin.ModelAdmin):
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
    list_editable = ["country_code"]
