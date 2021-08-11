from abc import ABCMeta, abstractstaticmethod

class ILaser(metaclass=ABCMeta):
    @abstractstaticmethod
    def get_impressoraLaser():
        """interface da impressora"""

class implaserHP(ILaser):
    def __init__(self):
        self.marca = 'HP'
        self.model = 'HP laser'
    
    def get_impressoraLaser(self):
        return {"Marca": self.marca, "Modelo": self.model}

class implaserEpson(ILaser):
    def __init__(self):
        self.marca = 'Epson'
        self.model = 'Epson laser'

    def get_impressoraLaser(self):
        return {"Marca": self.marca, "Modelo": self.model}

class laserFactory():

    @staticmethod
    def get_laser(laserFabrica):
        try:
            if laserFabrica == "implaserHP":
                return implaserHP()
            if laserFabrica == "implaserEpson":
                return implaserEpson()

            raise AssertionError("Impressora não identificada")
        except AssertionError as _e:
            print(_e)

if __name__ == "__main__":
    laser  = laserFactory.get_laser("implaserHP")
    print (f"{laser.__class__} : {laser.get_impressoraLaser()}")
    laser  = laserFactory.get_laser("implaserEpson")
    print (f"{laser.__class__} : {laser.get_impressoraLaser()}")