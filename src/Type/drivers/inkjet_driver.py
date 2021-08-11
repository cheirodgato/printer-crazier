from ...interfaces import DriverInterface


class InkjetDriver(DriverInterface):

    def __init__(self):
        self.__name = 'Inkjet_driver'
        self.__version = 0.1

    def driver_select(self):
        return {self.__name, self.__version}
