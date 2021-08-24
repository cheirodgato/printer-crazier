from abc import ABC, abstractmethod


class ILaser(ABC):

    @abstractmethod
    def get_impressora_laser(self):
        pass


class ImplaserHP(ILaser):
    def __init__(self):
        self.marca = 'HP'
        self.model = 'HP laser'

    def get_impressora_laser(self):
        print("Marca:", self.marca)
        print("Modelo:", self.model)
        print("------------------------------------------------------------")


class ImplaserEpson(ILaser):
    def __init__(self):
        self.marca = 'Epson'
        self.model = 'Epson laser'

    def get_impressora_laser(self):
        print("Marca:", self.marca)
        print("Modelo:", self.model)
        print("------------------------------------------------------------")


class LaserFactory:

    @staticmethod
    def get_laser_hp(self):
        return ImplaserHP().get_impressora_laser()

    @staticmethod
    def get_laser_epson(self):
        return ImplaserEpson().get_impressora_laser()
