from FabricaDeImpressora import ImpressoraHPFactory, ImpressoraEpsonFactory


class CriadorDeFabrica:
    @staticmethod
    def fabrica_epson():
        return ImpressoraEpsonFactory()

    @staticmethod
    def fabrica_hp():
        return ImpressoraHPFactory()
