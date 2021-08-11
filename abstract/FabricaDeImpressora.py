from abc import ABCMeta, abstractstaticmethod
from ImpressoraJatoDeTinta import JatoFactory
from ImpressoraLaser import laserFactory

class IFabricaDeImpressora(metaclass=ABCMeta):

    @abstractstaticmethod
    def get_impressora(tipo_impressora):
        """método de interface estática da impressora factory"""

class ImpressoraFactory(IFabricaDeImpressora):

    @staticmethod
    def get_impressora(tipo_impressora):
        try:
            if tipo_impressora in ["impjatoHP", "impjatoEpson"]:
                return JatoFactory.get_jato(tipo_impressora)
            if tipo_impressora in ["implaserHP", "implaserEpson"]:
                return laserFactory.get_laser(tipo_impressora)
            raise AssertionError("Impressora não encontrada")
        except AssertionError as _e:
            print(_e)
        return None
        
if __name__ == "__main__":
    impressora = ImpressoraFactory.get_impressora("")