from ..interfaces import PrinterInterface
from typing import Type


class Printer:

    def __init__(self, model, printer_type: Type[PrinterInterface]):
        self.model = model
        self.__printer_type = printer_type
