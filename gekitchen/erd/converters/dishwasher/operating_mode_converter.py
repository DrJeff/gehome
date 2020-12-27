import logging

from gekitchen.erd.converters.abstract import ErdReadOnlyConverter
from gekitchen.erd.converters.primitives import *
from gekitchen.erd.values.dishwasher import ErdOperatingMode, OperatingMode, OPERATING_MODE_MAP

_LOGGER = logging.getLogger(__name__)

class OperatingModeConverter(ErdReadOnlyConverter[OperatingMode]):
    def erd_decode(self, value: str) -> OperatingMode:
        """Decode the dishwasher operating state """
        try:
            om = ErdOperatingMode(value)
            _LOGGER.debug(f'raw operating mode value: {raw}')
            return OPERATING_MODE_MAP[om]
        except (KeyError, ValueError):
            return ErdOperatingMode.NA
