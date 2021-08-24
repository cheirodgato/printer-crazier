from abc import ABC, abstractmethod
from ImpressoraJatoDeTinta import JatoFactory
from ImpressoraLaser import LaserFactory


class IFabricaDeImpressora(ABC):

    @abstractmethod
    def make_impressora_laser(self) -> object:
        pass

    @abstractmethod
    def make_impressora_jato(self) -> object:
        pass


class ImpressoraHPFactory(IFabricaDeImpressora):

    def make_impressora_laser(self):
        return LaserFactory.get_laser_hp(self)

    def make_impressora_jato(self):
        return JatoFactory.get_jato_hp(self)


class ImpressoraEpsonFactory(IFabricaDeImpressora):

    def make_impressora_laser(self):
        return LaserFactory.get_laser_epson(self)

    def make_impressora_jato(self):
        return JatoFactory.get_jato_epson(self)