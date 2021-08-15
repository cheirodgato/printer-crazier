from abc import ABC, abstractmethod
from ImpressoraJatoDeTinta import JatoFactory
from ImpressoraLaser import LaserFactory


class IFabricaDeImpressora(ABC):

    @abstractmethod
    def get_impressora(self, tipo_impressora):
        pass


class ImpressoraFactory(IFabricaDeImpressora):

    def get_impressora(self, tipo_impressora):
        try:
            if tipo_impressora == "impjatoHP":
                return JatoFactory.get_jato(tipo_impressora)
            elif tipo_impressora == "implaserEpson":
                return LaserFactory.get_laser(tipo_impressora)
            raise AssertionError("Impressora não encontrada")
        except AssertionError as _e:
            print(_e)
        return None

if __name__ == "__main__":
    impressora = ImpressoraFactory.get_impressora
    print(f"{impressora.__class__} : {impressora.get_impressora_jato()}")