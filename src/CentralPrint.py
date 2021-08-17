from typing import List, Any

from CriadorDeFabrica import CriadorDeFabrica
from FabricaDeImpressora import IFabricaDeImpressora


class CentralPrint:
    impressoras: List[Any] = []

    def __init__(self):
        pass

    def __new__(cls):
        if not cls.__dict__.get('_instancia'):
            cls._instancia = object.__new__(cls)
        return cls._instancia

    @classmethod
    def get_instancia(cls):
        return cls()

    @classmethod
    def create(cls):
        EpsonLTDA = CriadorDeFabrica.fabrica_epson()
        HPLTDA = CriadorDeFabrica.fabrica_hp()

        cls.save(cls.make(EpsonLTDA))
        cls.save(cls.make(HPLTDA))

    @classmethod
    def save(cls, impressoras):
        cls.impressoras += impressoras

    def make(self: IFabricaDeImpressora):
        Laser = self.make_impressora_laser()
        Jato = self.make_impressora_jato()
        return [Laser, Jato]

    def show(self):
        for impressora in self.impressoras:
            print(impressora)
