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
        print("Marca:", self.marca)
        print("Modelo:", self.model)
        print("------------------------------------------------------------")


class ImpjatoEpson(IJato):
    def __init__(self):
        self.marca = 'Epson'
        self.model = 'Epson Jato de tinta'


    def get_impressora_jato(self):
        print("Marca:", self.marca)
        print("Modelo:", self.model)
        print("------------------------------------------------------------")


class JatoFactory:

    @staticmethod
    def get_jato_hp(self):
        return ImpjatoHP().get_impressora_jato()

    @staticmethod
    def get_jato_epson(self):
        return ImpjatoEpson().get_impressora_jato()

