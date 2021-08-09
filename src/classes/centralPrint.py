from typing import Type
from ..interfaces import Connection


class centralPrint:

    def __init__(self):
        self.printers = []

    def addPrinter(self, printer: Type[Connection]):
        self.printers.append(printer)
