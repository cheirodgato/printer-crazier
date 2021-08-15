from FabricaDeImpressora import ImpressoraFactory


class CriadorDeFabrica:

    def fabrica_epson(self, tipo):
        return ImpressoraFactory.get_impressora(tipo_impressora=tipo)

    def fabrica_hp(self, tipo):
        return ImpressoraFactory.get_impressora(tipo_impressora=tipo)


if __name__ == "__main__":
    epson = CriadorDeFabrica.fabrica_epson('impjatoHP')