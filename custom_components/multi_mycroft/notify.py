"""Mycroft AI notification platform."""
import logging

from mycroftapi import MycroftAPI

from homeassistant.components.notify import BaseNotificationService

from homeassistant.const import (
    CONF_IP_ADDRESS,
)

_LOGGER = logging.getLogger(__name__)


def get_service(hass, config, discovery_info=None):
    """Get the Multi Mycroft notification service."""
    return MultiMycroftNotificationService(
        config.get(CONF_IP_ADDRESS)
    )


class MultiMycroftNotificationService(BaseNotificationService):
    """The Multi Mycroft Notification Service."""

    def __init__(self, mycroft_ip):
        """Initialize the service."""
        self.mycroft_ip = mycroft_ip

    def send_message(self, message="", **kwargs):
        """Send a message to mycroft to speak on instance."""

        text = message
        mycroft = MycroftAPI(self.mycroft_ip)
        if mycroft is not None:
            mycroft.speak_text(text)
        else:
            _LOGGER.log("Could not reach this instance of mycroft")