from ..interfaces import DriverInterface
from typing import Type


class Manufacturer:

    def __init__(self, name, driver: Type[DriverInterface]):
        self.name = name
        self.__driver = driver
