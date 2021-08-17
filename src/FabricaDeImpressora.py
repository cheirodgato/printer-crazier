from abc import ABC, abstractmethod
from ImpressoraJatoDeTinta import JatoFactory
from ImpressoraLaser import LaserFactory


class IFabricaDeImpressora(ABC):

    @abstractmethod
    def make_impressora_laser():
        pass

    @abstractmethod
    def make_impressora_jato():
        pass


class ImpressoraHPFactory(IFabricaDeImpressora):
    @staticmethod
    def make_impressora_laser():
        return LaserFactory.get_laser_hp()

    @staticmethod
    def make_impressora_jato():
        return JatoFactory.get_jato_hp()


class ImpressoraEpsonFactory(IFabricaDeImpressora):
    @staticmethod
    def make_impressora_laser():
        return LaserFactory.get_laser_epson()

    @staticmethod
    def make_impressora_jato():
        return JatoFactory.get_jato_epson()
