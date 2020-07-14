"""Mycroft AI notification platform."""
import logging

import voluptuous as vol

from mycroftapi import MycroftAPI

from homeassistant.components.notify import (
    BaseNotificationService,
    PLATFORM_SCHEMA,
)

from homeassistant.helpers import config_validation as cv

from homeassistant.const import CONF_IP_ADDRESS

_LOGGER = logging.getLogger(__name__)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({vol.Required(CONF_IP_ADDRESS): cv.string})

def get_service(hass, config, discovery_info=None):
    """Get the Multi Mycroft notification service."""
    ip_address = config.get(CONF_IP_ADDRESS)
    return MultiMycroftNotificationService(hass, ip_address)


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