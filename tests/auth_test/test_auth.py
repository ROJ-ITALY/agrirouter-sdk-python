"""Tests agrirouter/auth/auth.py"""

from agrirouter import AuthUrlParameter
from agrirouter.auth.auth import Authorization
from tests.constants import (
    public_key,
    private_key,
    auth_result_url,
    ENV
)


class TestAuthorization:
    def test_extract_query_params(self):
        auth_client = Authorization(ENV, public_key=public_key, private_key=private_key)
        test_uri = "key1=val1&key2=val2&key3=val3"
        params = auth_client._extract_query_params(test_uri)
        assert params == {"key1": "val1", "key2": "val2", "key3": "val3"}

    def test_get_auth_request_url(self):
        auth_params = AuthUrlParameter(
            application_id="8c947a45-c57d-42d2-affc-206e21d63a50", response_type="onboard"
        )
        assert auth_params.state

        auth_client = Authorization(
            "QA", public_key=public_key, private_key=private_key
        )

        check_url = "https://agrirouter-qa.cfapps.eu10.hana.ondemand.com/application/" \
                    "8c947a45-c57d-42d2-affc-206e21d63a50/authorize?response_type=onboard&"
        result_url = auth_client.get_auth_request_url(auth_params)
        assert check_url == result_url.split("state")[0]

    def test_extract_auth_response(self):
        auth_client = Authorization(ENV, public_key=public_key, private_key=private_key)
        state = "3770a15d-adf3-4900-a435-464978fe8054"
        token = "token"
        signature = "signature"

        test_uri = f"www.my_response.com/app?state={state}&token={token}&signature={signature}"
        response = auth_client.extract_auth_response(test_uri)

        assert response.state == state
        assert response.signature == signature
        assert response.token == token
        assert not response.error
        assert response.is_successful

    def test_get_auth_result(self):
        auth_client = Authorization(
            "QA", public_key=public_key, private_key=private_key
        )
        auth_response = auth_client.extract_auth_response(auth_result_url)
        auth_client.verify_auth_response(auth_response)
        assert auth_response.get_auth_result().get_decoded_token()
