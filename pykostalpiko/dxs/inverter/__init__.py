"""Inverter specific DxsEntries."""
from pykostalpiko.dxs import Descriptor, ConfigurableDescriptor, MapperException


def _operation_status_mapper(val: int) -> str:
    """Map the operation status to a string."""

    if val == 0:
        return "Off"
    if val == 1:
        return "Idle"
    if val == 2:
        return "Starting"
    if val == 3:
        return "Feed MPP"
    if val == 4:
        return "Deactivated"
    if val == 5:
        return "Feed"
    raise MapperException("Failed mapping Operation Status", val)


OPERATION_STATUS = Descriptor(
    16780032, "Operation Status", mapper_function=_operation_status_mapper
)
SERIAL_NUMBER = Descriptor(16777728, "Serial Number")
ARTICLE_NUMBER = Descriptor(16777472, "Article Number")
COUNTRY_SETTINGS = Descriptor(16779522, "Country Settings")
COUNTRY_SETTINGS_VERSION = Descriptor(16779521, "Country Settings Version")

NAME = ConfigurableDescriptor(16777984, "Name")


# TODO: /settings/general/login

# TODO: /settings/communication/modem

# TODO: /settings/generator-configuration

# TODO: /settings/battery-configuration

# TODO: /settings/switching-output

# TODO: /settings/analog-inputs
