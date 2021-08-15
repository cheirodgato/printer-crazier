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
    def get_laser(laserFabrica):
        try:
            if laserFabrica == "implaserHP":
                return ImplaserHP()
            if laserFabrica == "implaserEpson":
                return ImplaserEpson()

            raise AssertionError("Impressora não identificada")
        except AssertionError as _e:
            print(_e)


if __name__ == "__main__":
    laser = LaserFactory.get_laser("implaserHP")
    print(f"{laser.__class__} : {laser.get_impressora_laser()}")
    laser = LaserFactory.get_laser("implaserEpson")
    print(f"{laser.__class__} : {laser.get_impressora_laser()}")
