from pykostalpiko.dxs import Descriptor, MapperException

CURRENT_DIRECTION_CHARING = "Charging"
CURRENT_DIRECTION_DISCHARGING = "Discharging"


def _batter_current_direction_mapper(self, val: int) -> str:
    """Map the battery current direction to a string."""

    if val == 0:
        return CURRENT_DIRECTION_DISCHARGING
    if val == 1:
        return CURRENT_DIRECTION_CHARING
    raise MapperException("Failed mapping Battery Current Direction", val)


VOLTAGE = Descriptor(33556226, "Battery Voltage", "V")
CHARGE = Descriptor(33556229, "Battery Charge", "%")
CURRENT = Descriptor(33556238, "Battery Current", "A")
CURRENT_DIRECTION = Descriptor(
    33556230,
    "Battery Current Direction",
    mapper_function=_batter_current_direction_mapper,
)
CYCLES = Descriptor(33556228, "Battery Cycles")
TEMPERATURE = Descriptor(33556227, "Battery Temperature", "°C")
