"""DxsEntris for day statistics."""
from pykostalpiko.dxs import Descriptor

YIELD = Descriptor(251658754, "Yield", "Wh")
HOME_CONSUMPTION = Descriptor(251659010, "Home Consumption", "Wh")
SELF_CONSUMPTION = Descriptor(251659266, "Self Consumption", "Wh")
SELF_CONSUMPTION_RATE = Descriptor(251659278, "Self Consumtion Rate", "%")
DEGREE_OF_SELF_SUFFICIENCY = Descriptor(251659279, "Degree of Self Sufficiency", "%")
