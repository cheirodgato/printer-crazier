from typing import Type

from CriadorDeFabrica import CriadorDeFabrica
from FabricaDeImpressora import IFabricaDeImpressora

class CentralPrint:
    impressorasDisponiveis = []

    def __init__(self):
        pass

    def __new__(cls):
        if not cls.__dict__.get('_instancia'):
            cls._instancia = object.__new__(cls)
        return cls._instancia

    @classmethod
    def get_instancia(cls):
        return cls()

    def make(self):
        Laser = self.make_impressora_laser()
        Jato = self.make_impressora_jato()
        return [Laser, Jato]

    @classmethod
    def create(cls):
        Fabrica = CriadorDeFabrica()

        EpsonLTDA = Fabrica.fabrica_epson()
        HPLTDA = Fabrica.fabrica_hp()

        cls.save(cls.make(EpsonLTDA))
        cls.save(cls.make(HPLTDA))

        return 0

    @classmethod
    def save(cls, impressoras: []):
        cls.impressorasDisponiveis = cls.impressorasDisponiveis + impressoras
