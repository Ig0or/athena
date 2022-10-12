# Standard
from enum import Enum


class CarColors(str, Enum):
    YELLOW = "YELLOW"
    BLUE = "BLUE"
    GRAY = "GRAY"


class CarModels(str, Enum):
    HATCH = "HATCH"
    SEDAN = "SEDAN"
    CONVERTIBLE = "CONVERTIBLE"
