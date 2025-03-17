import datetime
import json
import requests

from logistics.settings import TOKEN_KEY


def read_json(json_file: str):
    with open(json_file, mode="r", encoding="utf-8") as file:
        return json.load(file)


def make_request(**kwargs):
    # shipmentNumber
    # shipmentIdCreatTime
    # ShipmentOrg
    # shipmentOrgStir
    # shipmentCountryCode
    # shipmentCountry
    # shipmentSendOrg
    # shipmentDepartureTime
    # shipmentEnterUzb
    # shipmentProcessLocal
    # shipmentReceivedInd
    _id = kwargs.pop("correlationId")

    params = {
        "correlationId": _id,
        "data": dict(**kwargs),
        "dtl": datetime.datetime.now().date().isoformat(),
        "destinationSubscribers": [],
    }
    r = requests.post(
        "https://pushservice.egov.uz/v3/app/mq/receive",
        headers={"Authorization": f"Bearer {TOKEN_KEY}"},
        json=params,
    )
    print(r.text)
