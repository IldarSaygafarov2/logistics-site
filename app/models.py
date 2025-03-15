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
