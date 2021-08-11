from ...interfaces import DriverInterface


class LaserDriver(DriverInterface):

    def __init__(self):
        self.__name = 'Laser_driver'
        self.__version = 0.1

    def driver_select(self):
        return {self.__name, self.__version}
