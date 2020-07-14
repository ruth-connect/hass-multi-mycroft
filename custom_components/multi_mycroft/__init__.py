"""The Multiple Mycroft component."""
import logging

import voluptuous as vol

from homeassistant.const import CONF_IP_ADDRESS
from homeassistant.helpers import discovery
import homeassistant.helpers.config_validation as cv

_LOGGER = logging.getLogger(__name__)

DOMAIN = "multi_mycroft"

CONFIG_SCHEMA = vol.Schema(
    {DOMAIN: vol.Schema({vol.Required(CONF_IP_ADDRESS): cv.string})}, extra=vol.ALLOW_EXTRA
)


def setup(hass, config):
    """Set up the Multi Mycroft component."""
    hass.data[DOMAIN] = config[DOMAIN][IP_ADDRESS]
    discovery.load_platform(hass, "notify", DOMAIN, {}, config)
    return True