from abc import ABC, abstractmethod


class DriverInterface(ABC):

    @abstractmethod
    def driver_select(self):
        pass
