import unittest

from pspark.requests import Details, InvoiceRequest
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


class TestInvoiceRequest(unittest.TestCase):
    def test_dict_conversation_for_full_filled_object(self):
        details = Details(
            customer=Customer(
                first_name="first name",
                last_name="last name",
                email="email",
                phone="phone",
                customer_id="customer id",
                national_id="1234566789",
                taxpayer_identification_number="23456-33224",
                birthdate="1985-07-24",
            ),
            billing_info=BillingInfo(
                address="Address",
                country_code="IND",
                country="India",
                city="Mumbai",
                post_code="Country",
                region="Maharashtra",
                state="ON",
                payment_purpose="Payment purpose",
                street="Baker Street",
            ),
            crypto=Crypto(
                memo="Memo",
            ),
            bank=Bank(
                id="Bank ID",
                name="Bank Name",
                account="account",
                bic_code="AAAA-BB-CC-123",
            ),
            escrow_payment=EscrowPayment(
                payment_wallet_id="uuid",
            ),
            ui=Ui(
                language="en",
            ),
            web_data=WebData(
                ip="127.0.0.1",
                user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/51.0.2704.103 Safari/537.36",
                browser_color_depth=30,
                browser_language="en-GB,en-US;q=0.9,en;q=0.8",
                browser_screen_height=1080,
                browser_screen_width=1920,
                browser_timezone="Europe/Kiev",
                browser_timezone_offset=-120,
                browser_java_enabled=False,
                browser_java_script_enabled=True,
                browser_accept_header="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,"
                "/;q=0.8",
            ),
            card_data=CardData("4111111111111111"),
            payway=Payway(pwid="NGN-CARD-YIO1KO"),
        )

        dto = InvoiceRequest(
            wallet_id="79CDA5A3-C688-4996-8D20-3EDDF4E6B70B",
            reference="uuid",
            amount=100.50,
            return_url="http://example.com/return",
            details=details,
            title="title",
            description="description",
            callback_url="http://example.com/callback",
            nonce=1,
        )

        self.assertEqual(
            dto.as_dict(),
            {
                "amount": 100.5,
                "callback_url": "http://example.com/callback",
                "description": "description",
                "details": {
                    "bank": {
                        "account": "account",
                        "bic_code": "AAAA-BB-CC-123",
                        "id": "Bank ID",
                        "name": "Bank Name",
                    },
                    "billing_info": {
                        "address": "Address",
                        "city": "Mumbai",
                        "country": "India",
                        "country_code": "IND",
                        "payment_purpose": "Payment purpose",
                        "post_code": "Country",
                        "region": "Maharashtra",
                        "state": "ON",
                        "street": "Baker Street",
                    },
                    "card_data": {"number": "4111111111111111"},
                    "crypto": {"memo": "Memo"},
                    "customer": {
                        "birthdate": "1985-07-24",
                        "customer_id": "customer id",
                        "email": "email",
                        "first_name": "first name",
                        "last_name": "last name",
                        "national_id": "1234566789",
                        "phone": "phone",
                        "taxpayer_identification_number": "23456-33224",
                    },
                    "escrow_payment": {"payment_wallet_id": "uuid"},
                    "ui": {"language": "en"},
                    "web_data": {
                        "browser_accept_header": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,"
                        "image/apng,/;q=0.8",
                        "browser_color_depth": 30,
                        "browser_java_enabled": False,
                        "browser_java_script_enabled": True,
                        "browser_language": "en-GB,en-US;q=0.9,en;q=0.8",
                        "browser_screen_height": 1080,
                        "browser_screen_width": 1920,
                        "browser_timezone": "Europe/Kiev",
                        "browser_timezone_offset": -120,
                        "ip": "127.0.0.1",
                        "user_agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like "
                        "Gecko) Chrome/51.0.2704.103 Safari/537.36",
                    },
                    "payway": {"pwid": "NGN-CARD-YIO1KO"},
                },
                "nonce": 1,
                "reference": "uuid",
                "return_url": "http://example.com/return",
                "title": "title",
            },
        )
        self.assertEqual("79CDA5A3-C688-4996-8D20-3EDDF4E6B70B", dto.wallet_id)

    def test_dict_conversation_for_partially_filled_object(self):
        details = Details(
            customer=Customer(
                first_name="first name",
                last_name="last name",
                email="email",
                phone="phone",
            ),
            bank=Bank(
                id="Bank ID",
                name="Bank Name",
            ),
        )

        dto = InvoiceRequest(
            wallet_id="79CDA5A3-C688-4996-8D20-3EDDF4E6B70B",
            reference="uuid",
            amount=100.50,
            return_url="http://example.com/return",
            details=details,
            nonce=1,
        )

        self.assertEqual(
            dto.as_dict(),
            {
                "amount": 100.5,
                "details": {
                    "bank": {"id": "Bank ID", "name": "Bank Name"},
                    "customer": {
                        "email": "email",
                        "first_name": "first name",
                        "last_name": "last name",
                        "phone": "phone",
                    },
                },
                "nonce": 1,
                "reference": "uuid",
                "return_url": "http://example.com/return",
            },
        )

    def test_dict_conversation_for_empty_details_object(self):
        dto = InvoiceRequest(
            wallet_id="79CDA5A3-C688-4996-8D20-3EDDF4E6B70B",
            reference="uuid",
            amount=100.50,
            return_url="http://example.com/return",
            nonce=1,
        )

        self.assertEqual(
            dto.as_dict(),
            {
                "amount": 100.5,
                "nonce": 1,
                "reference": "uuid",
                "return_url": "http://example.com/return",
            },
        )

    def test_callback_url_validation(self):
        with self.assertRaises(
            ValueError, msg="InvoiceRequest callback_url validation failed."
        ):
            InvoiceRequest(
                wallet_id="79CDA5A3-C688-4996-8D20-3EDDF4E6B70B",
                reference="uuid",
                amount=100.50,
                return_url="http://example.com/return",
                callback_url="invalid_url",
                nonce=1,
            )

    def test_return_url_validation(self):
        with self.assertRaises(
            ValueError, msg="InvoiceRequest return_url validation failed."
        ):
            InvoiceRequest(
                wallet_id="79CDA5A3-C688-4996-8D20-3EDDF4E6B70B",
                reference="uuid",
                amount=100.50,
                return_url="invalid_url",
                nonce=1,
            )
