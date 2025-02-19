"""Test agrirouter/revoking/parameters.py"""

from agrirouter import RevokingParameter
from tests.constants import application_id


class TestRevokingParameter:
    content_type = "json"
    account_id = "111"
    endpoint_ids = "endpoint_1"
    time_zone = "+03:00"
    utc_timestamp = "01-01-2021"
    test_object = RevokingParameter(
        application_id=application_id,
        content_type=content_type,
        account_id=account_id,
        endpoint_ids=endpoint_ids,
        utc_timestamp=utc_timestamp,
        time_zone=time_zone
    )

    def test_get_header_params(self):
        assert self.test_object.get_header_params()["application_id"] == application_id
        assert self.test_object.get_header_params()["content_type"] == self.content_type

    def test_get_body_params(self):
        assert self.test_object.get_body_params()["account_id"] == self.account_id
        assert self.test_object.get_body_params()["endpoint_ids"] == self.endpoint_ids
        assert self.test_object.get_body_params()["utc_timestamp"] == self.utc_timestamp
        assert self.test_object.get_body_params()["time_zone"] == self.time_zone
