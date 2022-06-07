"""DxsEntries for total statistics."""
from pykostalpiko.dxs import Descriptor

YIELD = Descriptor(251658753, "Yield", "Wh", multiplication_factor=1000)
HOME_CONSUMPTION = Descriptor(
    251659009, "Home Consumption", "Wh", multiplication_factor=1000
)
SELF_CONSUMPTION = Descriptor(
    251659265, "Self Consumption", "Wh", multiplication_factor=1000
)
SELF_CONSUMPTION_RATE = Descriptor(251659280, "Self Consumtion Rate", "%")
DEGREE_OF_SELF_SUFFICIENCY = Descriptor(251659281, "Degree of Self Sufficiency", "%")
OPERATION_TIME = Descriptor(251658496, "Operation Time", "h")
