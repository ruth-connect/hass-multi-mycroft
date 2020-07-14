"""The Multiple Mycroft component."""
import logging

import voluptuous as vol

from homeassistant.const import CONF_NAME, CONF_IP_ADDRESS
from homeassistant.helpers import discovery
import homeassistant.helpers.config_validation as cv

_LOGGER = logging.getLogger(__name__)

ENTITY_ID_FORMAT = "multi_mycroft.{}"

CREATE_FIELDS = {
    vol.Required(CONF_NAME): cv.string,
    vol.Required(CONF_IP_ADDRESS): cv.string,
}

CONFIG_SCHEMA = vol.Schema(
    {
        vol.Optional(DOMAIN, default=[]): vol.Any(
            vol.All(cv.ensure_list, [vol.Schema(CREATE_FIELDS)])
        )
    },
    extra=vol.ALLOW_EXTRA,
)


def setup(hass, config):
    return True

def setup_entry(hass, entry):
    _LOGGER.error("RUTH: %s, %s, %s", config[DOMAIN], config[CONF_NAME], config[CONF_IP_ADDRESS])
    hass.data[DOMAIN] = config[DOMAIN][CONF_NAME][CONF_IP_ADDRESS]
    discovery.load_platform(hass, "notify", DOMAIN, {}, config)
    return True