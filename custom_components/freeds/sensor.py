"""Support for freeds via MQTT"""

import logging

from homeassistant.components.sensor import ENTITY_ID_FORMAT

from homeassistant.helpers.entity import Entity, async_generate_entity_id

from . import DOMAIN as FREEDS_DOMAIN


_LOGGER = logging.getLogger(__name__)