from CriadorDeFabrica import CriadorDeFabrica
from FabricaDeImpressora import *
from ImpressoraJatoDeTinta import *
from ImpressoraLaser import *

class CentralPrint:
    impressorasDisponiveis = []

    def __new__(cls):
        if not cls.__dict__.get('_instancia'):
            cls._instancia = object.__new__(cls)
        return cls._instancia

    @classmethod
    def get_instancia(cls):
        return cls()

    def gerar_impressora(fabrica):
        impressoraLaser = fabrica.criarImpressaLaser()
        impressoraJatoDeTinta = fabrica.criarImpressoraJatoDeTinta()
        return [impressoraLaser, impressoraJatoDeTinta]

    @classmethod
    def criacao(cls):
        fab = CriadorDeFabrica()
        print('### Gerando fabricas')
        fabEpson = fab.criarFabricaEpson()
        fabHP = fab.criarFabricaHP()
        print('### Gerando Impressoras')
        cls.salvaImpressoras(cls.gerarImpressora(fabEpson))
        cls.salvaImpressoras(cls.gerarImpressora(fabHP))
        print('Impressoras criadas e disponpiveis para uso')
        return 0

    @classmethod
    def salvaImpressoras(cls, impressoras: []):
        cls.impressorasDisponiveis = cls.impressorasDisponiveis + impressoras

    def testarImpressorasDisponiveis(self):
        for impressora in self.impressorasDisponiveis:
            impressora.imprimir()
        print('Quantidade de impressoras ', len(self.impressorasDisponiveis))
        return 0
        return cls()
