"""The Multiple Mycroft component."""
import logging

import voluptuous as vol

from homeassistant.const import CONF_NAME, CONF_IP_ADDRESS
from homeassistant.helpers import discovery
import homeassistant.helpers.config_validation as cv

_LOGGER = logging.getLogger(__name__)

CONFIG_SCHEMA = vol.Schema(
    {vol.Required(CONF_NAME): cv.string, vol.Required(CONF_IP_ADDRESS): cv.string},
    extra=vol.ALLOW_EXTRA,
)

def setup(hass, config):
    return True

def setup_entry(hass, entry):
    hass.data[DOMAIN] = config[DOMAIN][CONF_NAME][CONF_IP_ADDRESS]
    discovery.load_platform(hass, "notify", DOMAIN, {}, config)
    return True