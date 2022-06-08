from pykostalpiko.dxs.current_values import LIST as current_values_LIST
from pykostalpiko.dxs.entry import Descriptor
from pykostalpiko.dxs.statistics import LIST as statistics_LIST
from pykostalpiko.dxs.inverter import LIST as inverter_LIST

LIST = current_values_LIST + statistics_LIST + inverter_LIST


def find_descriptor_by_id(id: int) -> Descriptor:
    """Find a descriptor by its id."""
    for descriptor in LIST:
        if descriptor.key == id:
            return descriptor

    raise ValueError(f"No descriptor found for id {id}")
