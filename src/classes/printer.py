from typing import Type
from .printerType import PrinterType


class Printer:

    def __init__(self, alias, model):
        self.__printing = False
        self.alias = alias
        self.model = model
        self.type = Type[PrinterType]
        self.driver = Type[PrinterType]

    def print(self):
        print('Printing...')
        self.__printing = True

    def getModel(self):
        return self.model

    def getType(self):
        return self.type

    def getDriver(self):
        return self.driver
