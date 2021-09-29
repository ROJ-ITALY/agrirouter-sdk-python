from urllib.parse import urlparse, parse_qs

from auth.parameters import AuthUrlParameter
from auth.response import AuthResponse
from environments.environmental_services import EnvironmentalService


class Authorization(EnvironmentalService):

    SIGNATURE_KEY = "signature"
    STATE_KEY = "state"
    TOKEN_KEY = "token"
    ERROR_KEY = "error"

    def __init__(self, *args, **kwargs):
        self._public_key = kwargs.pop("public_key")
        self._private_key = kwargs.pop("private_key")
        super(Authorization, self).__init__(*args, **kwargs)

    def get_auth_request_url(self, parameters: AuthUrlParameter) -> str:
        auth_parameters = parameters.get_parameters()
        return self._environment.get_secured_onboarding_authorization_url(**auth_parameters)

    def extract_auth_response(self, url: str) -> AuthResponse:
        parsed_url = urlparse(url)
        query_params = self._extract_query_params(parsed_url.query)
        return AuthResponse(query_params)

    @staticmethod
    def verify_auth_response(response, public_key):
        response.verify(public_key)

    @staticmethod
    def _extract_query_params(query_params: str) -> dict:
        qp_pairs = parse_qs(query_params)
        return {k: v[0] for k, v in qp_pairs.items()}

