import unittest

from httpx import Response, TimeoutException

from pspark import PSPark
from pspark.exceptions import (
    HttpClientException,
    HttpRedirectionException,
    HttpServerException,
    HttpTimeoutException,
    ResponseValidationException,
)
from pspark.requests import BalancesRequest

import respx

from tests.helper import generate_jwt_key


class TestAbstractHttpClientWrapper(unittest.TestCase):
    @respx.mock
    def test_http_server_exception(self):
        route = respx.post("https://api.ppark.io/v1/balances").mock(
            return_value=Response(500)
        )

        sdk = PSPark(jwt_key=generate_jwt_key(), api_key="api_key")

        with self.assertRaises(HttpServerException) as context:
            sdk.get_balances(BalancesRequest())

        self.assertTrue(route.called)
        self.assertIsInstance(context.exception, HttpServerException)

    @respx.mock
    def test_http_client_exception(self):
        route = respx.post("https://api.ppark.io/v1/balances").mock(
            return_value=Response(400)
        )

        sdk = PSPark(jwt_key=generate_jwt_key(), api_key="api_key")

        with self.assertRaises(HttpClientException) as context:
            sdk.get_balances(BalancesRequest())

        self.assertTrue(route.called)
        self.assertIsInstance(context.exception, HttpClientException)

    @respx.mock
    def test_http_redirect_exception(self):
        route = respx.post("https://api.ppark.io/v1/balances").mock(
            return_value=Response(300)
        )

        sdk = PSPark(jwt_key=generate_jwt_key(), api_key="api_key")

        with self.assertRaises(HttpRedirectionException) as context:
            sdk.get_balances(BalancesRequest())

        self.assertTrue(route.called)
        self.assertIsInstance(context.exception, HttpRedirectionException)

    @respx.mock
    def test_response_validation_exception(self):
        route = respx.post("https://api.ppark.io/v1/balances").mock(
            return_value=Response(
                200, json={"code": 1002, "message": "Request Data Error"}
            )
        )

        sdk = PSPark(jwt_key=generate_jwt_key(), api_key="api_key")

        with self.assertRaises(ResponseValidationException) as context:
            sdk.get_balances(BalancesRequest())

        self.assertTrue(route.called)
        self.assertIsInstance(context.exception, ResponseValidationException)
        self.assertEqual(context.exception.code, 1002)
        self.assertEqual(context.exception.message, "Request Data Error")

    @respx.mock
    def test_http_timeout_exception(self):
        route = respx.post("https://api.ppark.io/v1/balances").mock(
            side_effect=TimeoutException
        )

        sdk = PSPark(jwt_key=generate_jwt_key(), api_key="api_key")

        with self.assertRaises(HttpTimeoutException) as context:
            sdk.get_balances(BalancesRequest())

        self.assertTrue(route.called)
        self.assertIsInstance(context.exception, HttpTimeoutException)
