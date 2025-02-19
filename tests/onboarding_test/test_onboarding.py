"""Test agrirouter/onboarding/onboarding.py"""

from agrirouter.onboarding.exceptions import WrongCertificationType, WrongGateWay
from agrirouter.onboarding.onboarding import SoftwareOnboarding
from agrirouter.onboarding.parameters import SoftwareOnboardingParameter
from agrirouter.onboarding.enums import GateWays, CertificateTypes
from tests.constants import public_key, private_key, ENV, application_id
import pytest


class TestSoftwareOnboarding:
    def test__create_request(self):
        params = SoftwareOnboardingParameter(
            id_=1,
            application_id=application_id,
            content_type="json",
            certification_version_id="13",
            gateway_id=GateWays.MQTT.value,
            certificate_type=CertificateTypes.PEM.value,
            utc_timestamp="+03:00",
            time_zone="01-01-2021",
            reg_code="8eloz190fd",
        )
        onboarding = SoftwareOnboarding(
            public_key=public_key, private_key=private_key, env=ENV
        )
        assert onboarding._create_request(params, "localhost")

        params = SoftwareOnboardingParameter(
            id_=2,
            application_id=application_id,
            content_type="json",
            certification_version_id="13",
            gateway_id=GateWays.MQTT.value,
            certificate_type="wrong_certificate",
            utc_timestamp="+03:00",
            time_zone="01-01-2021",
            reg_code="8eloz190fd",
        )
        onboarding = SoftwareOnboarding(
            public_key=public_key, private_key=private_key, env=ENV
        )
        with pytest.raises(WrongCertificationType):
            assert onboarding._create_request(params, "localhost")

        params = SoftwareOnboardingParameter(
            id_=3,
            application_id=application_id,
            content_type="content_type",
            certification_version_id="13",
            gateway_id="wrong_gateway_id",
            certificate_type=CertificateTypes.PEM.value,
            utc_timestamp="+03:00",
            time_zone="01-01-2021",
            reg_code="8eloz190fd",
        )
        onboarding = SoftwareOnboarding(
            public_key=public_key, private_key=private_key, env=ENV
        )
        with pytest.raises(WrongGateWay):
            assert onboarding._create_request(params, "localhost")
