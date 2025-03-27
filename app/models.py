import uuid
from django.db import models
from utils.main import read_json, make_request
from enum import StrEnum

COUNTRY_CHOICES = [
    (item["code"], f'{item["name"]}') for item in read_json("countries.json")
]


class TrackStatus(StrEnum):
    pass


class TrackInfo(models.Model):
    correlation_id = models.UUIDField(default=uuid.uuid4)
    shipment_number = models.CharField(max_length=100, verbose_name="Трек номер")
    shipment_id_create_time = models.DateField(
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
        verbose_name="Название страны отправителя", max_length=60, default="Корея"
    )
    shop_name = models.CharField(verbose_name="Название магазина", max_length=100)
    shipment_departure_time = models.DateField(
        verbose_name="Дата отправки груза",
        help_text="Дата отправки груза из страны отправителя",
        null=True,
        blank=True,
    )
    shipment_enter_uzb = models.DateField(
        verbose_name="Дата прилета",
        help_text="Дата прилета в страну назначения",
        null=True,
        blank=True,
    )
    shipment_process_local = models.DateField(
        verbose_name="Дата принятия на склад",
        help_text="Когда посылка была принята на склад",
        null=True,
        blank=True,
    )
    shipment_received_time = models.DateField(
        verbose_name="Дата доставки",
        help_text="Дата доставки посылки получателю",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.shipment_number

    def save(self, *args, **kwargs):

        make_request(
            correlationId=str(self.correlation_id),
            shipmentNumber=self.shipment_number,
            shipmentIdCreatTime=self.shipment_id_create_time.isoformat(),
            ShipmentOrg=self.shop_name,
            shipmentOrgStir=self.inn,
            shipmentCountryCode=self.country_code,
            shipmentCountry=self.county_name,
            shipmentSendOrg=self.shipment_org_name,
            shipmentDepartureTime=self.shipment_departure_time.isoformat(),
            shipmentEnterUzb=self.shipment_enter_uzb.isoformat(),
            shipmentProcessLocal=self.shipment_process_local.isoformat(),
            shipmentReceivedInd=self.shipment_received_time.isoformat(),
        )
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Данные о грузе"
        verbose_name_plural = "Данные о грузах"


class RequestMessage(models.Model):
    first_name = models.CharField(verbose_name="Имя", max_length=150)
    email = models.EmailField(verbose_name="Почта")
    subject = models.CharField(verbose_name="Тема", max_length=150)
    message = models.TextField(verbose_name="Сообщение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.first_name} - {self.subject}"

    class Meta:
        verbose_name = "Сообщение с сайта"
        verbose_name_plural = "Сообщения с сайта"
