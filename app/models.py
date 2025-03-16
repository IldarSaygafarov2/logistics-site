from django.db import models
from utils.main import read_json


COUNTRY_CHOICES = [
    (item["code"], f'{item["name"]}-{item["code"]}')
    for item in read_json("countries.json")
]


class TrackInfo(models.Model):
    shipment_number = models.CharField(max_length=100, verbose_name="Трек номер")
    shipment_id_create_time = models.DateTimeField(
        verbose_name="Дата формирования заказа",
        help_text="Когда сформирован заказ на складе отправителя",
    )
    shipment_org_name = models.CharField(
        verbose_name="Наименование курьерской организации",
        max_length=200,
        default="NEW AVIA LOGISTIC",
    )
    inn = models.CharField(verbose_name="ИНН", max_length=10, default="308646036")
    country_code = models.CharField(
        choices=COUNTRY_CHOICES, verbose_name="Код страны", max_length=5
    )
    county_name = models.CharField(
        verbose_name="Название страны отправителя", max_length=60
    )
    shop_name = models.CharField(verbose_name="Название магазина", max_length=100)
    shipment_departure_time = models.DateTimeField(
        verbose_name="Дата отправки груза",
        help_text="Дата отправки груза из страны отправителя",
    )
    shipment_enter_uzb = models.DateTimeField(
        verbose_name="Дата прилета", help_text="Дата прилета в страну назначения"
    )
    shipment_process_local = models.DateTimeField(
        verbose_name="Дата принятия на склад",
        help_text="Когда посылка была принята на склад",
    )
    shipment_received_time = models.DateTimeField(
        verbose_name="Дата доставки", help_text="Дата доставки посылки получателю"
    )

    def __str__(self):
        return self.shipment_number

    class Meta:
        verbose_name = "Данные о грузе"
        verbose_name_plural = "Данные о грузах"
