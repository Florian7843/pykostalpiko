"""RS485 specific DxsEntries."""
from pykostalpiko.dxs import MapperException, ConfigurableDescriptor


def _protocol_mapper(val: int) -> str:
    """Map the protocol to a string."""

    if val == 0:
        return "KOSTAL"
    if val == 1:
        return "Modbus"
    raise MapperException("Failed mapping Protocol", val)


BUS_TERMINATION = ConfigurableDescriptor(117441027, "Bus Termination")
BUS_BIAS_VOLTAGE = ConfigurableDescriptor(117441026, "Bus Bias Voltage")
PROTOCOL = ConfigurableDescriptor(
    117441028, "Protocol", mapper_function=_protocol_mapper
)
BAUD_RATE = ConfigurableDescriptor(117441029, "Baud Rate")
