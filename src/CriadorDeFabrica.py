from FabricaDeImpressora import ImpressoraHPFactory, ImpressoraEpsonFactory


class CriadorDeFabrica:

    def fabrica_epson(self):
        return ImpressoraEpsonFactory()

    def fabrica_hp(self):
        return ImpressoraHPFactory()
