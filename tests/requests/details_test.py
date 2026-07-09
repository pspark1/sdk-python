import unittest

from pspark.requests import Details
from pspark.requests.details_dto import (
    Bank,
    BillingInfo,
    CardData,
    Crypto,
    Customer,
    EscrowPayment,
    Payway,
    Ui,
    WebData,
)
from pspark.requests.details_dto.project import Project


class TestDetails(unittest.TestCase):
    def test_dict_conversation(self):
        dto = Details(
            customer=Customer(
                first_name="first name",
                last_name="last name",
                customer_id="customer id",
            ),
            billing_info=BillingInfo("Address"),
            crypto=Crypto("Memo"),
            bank=Bank("Bank id"),
            escrow_payment=EscrowPayment("uuid"),
            ui=Ui("en"),
            web_data=WebData(user_agent="Firefox"),
            card_data=CardData("4111111111111111"),
            project=Project("https://example.com"),
            payway=Payway(pwid="NGN-CARD-YIO1KO"),
        )

        self.assertEqual(
            dto.as_dict(),
            {
                "customer": {
                    "customer_id": "customer id",
                    "first_name": "first name",
                    "last_name": "last name",
                },
                "billing_info": {"address": "Address"},
                "crypto": {"memo": "Memo"},
                "bank": {"id": "Bank id"},
                "escrow_payment": {"payment_wallet_id": "uuid"},
                "ui": {"language": "en"},
                "web_data": {"user_agent": "Firefox"},
                "card_data": {"number": "4111111111111111"},
                "project": {"url": "https://example.com"},
                "payway": {"pwid": "NGN-CARD-YIO1KO"},
            },
        )

    def test_empty_dict_conversation(self):
        dto = Details()

        self.assertEqual(dto.as_dict(), {})
