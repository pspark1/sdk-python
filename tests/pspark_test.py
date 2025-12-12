import unittest

from httpx import Response

from pspark import PSPark
from pspark.requests import (
    AddressRequest,
    BalanceRequest,
    BalancesRequest,
    InvoiceRequest,
    RateRequest,
    TransactionRequest,
    WithdrawalRequest,
)

import respx

from tests.helper import generate_jwt_key


class TestPSPark(unittest.TestCase):
    @respx.mock
    def test_send_headers(self):
        route = respx.post("https://api.ppark.io/v1/balances").mock(
            return_value=Response(200, json={})
        )

        sdk = PSPark(jwt_key=generate_jwt_key(), api_key="api_key")

        sdk.get_balances(BalancesRequest())

        headers = route.calls[0].request.headers

        self.assertIn("Authorization", headers)
        self.assertEqual("api_key", headers["X-Api-Key"])

    @respx.mock
    def test_get_balances(self):
        route = respx.post("https://api.ppark.io/v1/balances").mock(
            return_value=Response(200, json={"code": 0, "message": "Ok"})
        )

        sdk = PSPark(jwt_key=generate_jwt_key(), api_key="api_key")

        response = sdk.get_balances(BalancesRequest())

        self.assertTrue(route.called)
        self.assertEqual(200, response.status_code)
        self.assertEqual({"code": 0, "message": "Ok"}, response.json())

    @respx.mock
    def test_get_balance(self):
        route = respx.post(
            "https://api.ppark.io/v1/wallet/79CDA5A3-C688-4996-8D20-3EDDF4E/balance"
        ).mock(return_value=Response(200, json={"code": 0, "message": "Ok"}))

        sdk = PSPark(jwt_key=generate_jwt_key(), api_key="api_key")

        response = sdk.get_balance(
            BalanceRequest(wallet_id="79CDA5A3-C688-4996-8D20-3EDDF4E")
        )

        self.assertTrue(route.called)
        self.assertEqual(200, response.status_code)
        self.assertEqual({"code": 0, "message": "Ok"}, response.json())

    @respx.mock
    def test_create_address(self):
        route = respx.post(
            "https://api.ppark.io/v1/wallet/79CDA5A3-C688-4996-8D20-3EDDF4E/address/create"
        ).mock(return_value=Response(200, json={"code": 0, "message": "Ok"}))

        sdk = PSPark(jwt_key=generate_jwt_key(), api_key="api_key")

        response = sdk.create_address(
            AddressRequest(
                wallet_id="79CDA5A3-C688-4996-8D20-3EDDF4E",
                reference="uuid",
            )
        )

        self.assertTrue(route.called)
        self.assertEqual(200, response.status_code)
        self.assertEqual({"code": 0, "message": "Ok"}, response.json())

    @respx.mock
    def test_create_withdrawal(self):
        route = respx.post(
            "https://api.ppark.io/v1/wallet/79CDA5A3-C688-4996-8D20-3EDDF4E/withdrawal/create"
        ).mock(return_value=Response(200, json={"code": 0, "message": "Ok"}))

        sdk = PSPark(jwt_key=generate_jwt_key(), api_key="api_key")

        response = sdk.create_withdrawal(
            WithdrawalRequest(
                wallet_id="79CDA5A3-C688-4996-8D20-3EDDF4E",
                reference="uuid",
                amount=100,
                account="account",
            )
        )

        self.assertTrue(route.called)
        self.assertEqual(200, response.status_code)
        self.assertEqual({"code": 0, "message": "Ok"}, response.json())

    @respx.mock
    def test_create_invoice(self):
        route = respx.post(
            "https://api.ppark.io/v1/wallet/79CDA5A3-C688-4996-8D20-3EDDF4E/invoice/create"
        ).mock(return_value=Response(200, json={"code": 0, "message": "Ok"}))

        sdk = PSPark(jwt_key=generate_jwt_key(), api_key="api_key")

        response = sdk.create_invoice(
            InvoiceRequest(
                wallet_id="79CDA5A3-C688-4996-8D20-3EDDF4E",
                reference="uuid",
                amount=100,
                return_url="http://example.com",
            )
        )

        self.assertTrue(route.called)
        self.assertEqual(200, response.status_code)
        self.assertEqual({"code": 0, "message": "Ok"}, response.json())

    @respx.mock
    def test_get_transaction_status(self):
        route = respx.post(
            "https://api.ppark.io/v1/wallet/79CDA5A3-C688-4996-8D20-3EDDF4E/transaction/status"
        ).mock(return_value=Response(200, json={"code": 0, "message": "Ok"}))

        sdk = PSPark(jwt_key=generate_jwt_key(), api_key="api_key")

        response = sdk.get_transaction_status(
            TransactionRequest(
                wallet_id="79CDA5A3-C688-4996-8D20-3EDDF4E",
                reference="uuid",
            )
        )

        self.assertTrue(route.called)
        self.assertEqual(200, response.status_code)
        self.assertEqual({"code": 0, "message": "Ok"}, response.json())

    @respx.mock
    def test_get_rates(self):
        route = respx.post("https://api.ppark.io/v1/rates").mock(
            return_value=Response(200, json={"code": 0, "message": "Ok"})
        )

        sdk = PSPark(jwt_key=generate_jwt_key(), api_key="api_key")

        response = sdk.get_rates(RateRequest("DOGE", "USD"))

        self.assertTrue(route.called)
        self.assertEqual(200, response.status_code)
        self.assertEqual({"code": 0, "message": "Ok"}, response.json())
