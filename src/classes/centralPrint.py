from typing import Type, Union


class CentralPrint:

    def __init__(self):
        self.__instance: Union[Type[CentralPrint], None] = None
        self.__printers = []

    def add_printer(self):
        return self.printers.append([''])

    def remove_printer(self):
        pass

    def show_connections(self):
        pass
