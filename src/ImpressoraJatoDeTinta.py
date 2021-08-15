from abc import ABC, abstractmethod


class IJato(ABC):
    @abstractmethod
    def get_impressora_jato(self):
        pass


class ImpjatoHP(IJato):
    def __init__(self):
        self.marca = 'HP'
        self.model = 'HP Jato de tinta'

    def get_impressora_jato(self):
        return {"Marca": self.marca, "Modelo": self.model}


class ImpjatoEpson(IJato):
    def __init__(self):
        self.marca = 'Epson'
        self.model = 'Epson Jato de tinta'

    def get_impressora_jato(self):
        return {"Marca": self.marca, "Modelo": self.model}


class JatoFactory():

    @staticmethod
    def get_jato(jatoFabrica):
        try:
            if jatoFabrica == "impjatoHP":
                return ImpjatoHP()
            if jatoFabrica == "impjatoEpson":
                return ImpjatoEpson()

            raise AssertionError("Impressora não identificada")
        except AssertionError as _e:
            print(_e)


if __name__ == "__main__":
    JATO = JatoFactory.get_jato("impjatoHP")
    print(f"{JATO.__class__} : {JATO.get_impressora_jato()}")
    JATO = JatoFactory.get_jato("impjatoEpson")
    print(f"{JATO.__class__} : {JATO.get_impressora_jato()}")
