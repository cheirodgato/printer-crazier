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


class JatoFactory:

    @staticmethod
    def get_jato_hp(self):
        return ImpjatoHP()

    @staticmethod
    def get_jato_epson(self):
        return ImpjatoEpson()

if __name__ == "__main__":
    JATO = JatoFactory.get_jato_hp("impjatoHP")
    print(f"{JATO.__class__} : {JATO.get_impressora_jato()}")
    JATO = JatoFactory.get_jato_epson("impjatoEpson")
    print(f"{JATO.__class__} : {JATO.get_impressora_jato()}")
