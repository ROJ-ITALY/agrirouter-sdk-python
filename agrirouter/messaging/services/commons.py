import os
from abc import ABC, abstractmethod

import requests

from agrirouter.messaging.certification import create_certificate_file_from_pen
from agrirouter.messaging.clients.http import HttpClient
from agrirouter.messaging.clients.mqtt import MqttClient
from agrirouter.messaging.messages import Message
from agrirouter.messaging.request import MessageRequest
from agrirouter.messaging.result import MessagingResult
from agrirouter.onboarding.exceptions import BadMessagingResult


class AbstractMessagingClient(ABC):

    @staticmethod
    def create_message_request(parameters) -> MessageRequest:
        messages = []
        for encoded_message in parameters.get_encoded_messages():
            message = Message(encoded_message)
            messages.append(message.json_serialize())
        message_request = MessageRequest(
            parameters.get_onboarding_response().get_sensor_alternate_id(),
            parameters.get_onboarding_response().get_capability_alternate_id(),
            messages
        )
        return message_request

    @abstractmethod
    def send(self, parameters):
        ...


class HttpMessagingService(AbstractMessagingClient):

    def __init__(self, on_message_callback):
        self.client = HttpClient(on_message_callback=on_message_callback)

    def send(self, parameters) -> MessagingResult:
        request = self.create_message_request(parameters)
        response = self.client.send(
            "POST",
            parameters.get_onboarding_response(),
            request
        )
        if response.status in [400, 401, 403, 404, 500]:
            raise BadMessagingResult(f"Messaging Request failed with status code {response.status}")
        result = MessagingResult([parameters.get_application_message_id()])
        return result

    def subscribe(self):
        pass

    def unsubscribe(self):
        pass


class MqttMessagingService(AbstractMessagingClient):

    def __init__(self,
                 onboarding_response,
                 on_message_callback: callable = None,
                 ):

        self.onboarding_response = onboarding_response
        self.client = MqttClient(
            client_id=self.onboarding_response.get_client_id(),
            on_message_callback=on_message_callback,
        )
        self.client.connect(
            self.onboarding_response.get_connection_criteria().get_host(),
            self.onboarding_response.get_connection_criteria().get_port()
        )

    def send(self, parameters, qos: int = 0) -> MessagingResult:
        mqtt_payload = self.create_message_request(parameters)
        self.client.publish(
            self.onboarding_response.get_connection_criteria().get_measures(), mqtt_payload,
            qos=qos
        )
        result = MessagingResult([parameters.get_application_message_id()])
        return result

    def subscribe(self):
        pass

    def unsubscribe(self):
        pass
