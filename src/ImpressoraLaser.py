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
        return {"Marca": self.marca, "Modelo": self.model}


class ImplaserEpson(ILaser):
    def __init__(self):
        self.marca = 'Epson'
        self.model = 'Epson laser'

    def get_impressora_laser(self):
        return {"Marca": self.marca, "Modelo": self.model}


class LaserFactory:

    @staticmethod
    def get_laser_hp(self):
        return ImplaserHP()

    @staticmethod
    def get_laser_epson(self):
        return ImplaserEpson()


# if __name__ == "__main__":
#     laser = LaserFactory.get_laser("implaserHP")
#     print(f"{laser.__class__} : {laser.get_impressora_laser()}")
#     laser = LaserFactory.get_laser("implaserEpson")
#     print(f"{laser.__class__} : {laser.get_impressora_laser()}")
