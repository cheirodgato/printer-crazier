from abc import ABC, abstractmethod


class PrinterInterface(ABC):

    @abstractmethod
    def printer_select(self):
        pass
