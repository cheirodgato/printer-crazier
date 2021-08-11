from abc import ABCMeta, abstractstaticmethod

class IJato(metaclass=ABCMeta):
    @abstractstaticmethod
    def get_impressoraJato():
        """interface da impressora"""

class impjatoHP(IJato):
    def __init__(self):
        self.marca = 'HP'
        self.model = 'HP Jato de tinta'
    
    def get_impressoraJato(self):
        return {"Marca": self.marca, "Modelo": self.model}

class impjatoEpson(IJato):
    def __init__(self):
        self.marca = 'Epson'
        self.model = 'Epson Jato de tinta'

    def get_impressoraJato(self):
        return {"Marca": self.marca, "Modelo": self.model}

class JatoFactory():

    @staticmethod
    def get_jato(jatoFabrica):
        try:
            if jatoFabrica == "impjatoHP":
                return impjatoHP()
            if jatoFabrica == "impjatoEpson":
                return impjatoEpson()

            raise AssertionError("Impressora não identificada")
        except AssertionError as _e:
            print(_e)

if __name__ == "__main__":
    JATO  = JatoFactory.get_jato("impjatoHP")
    print (f"{JATO.__class__} : {JATO.get_impressoraJato()}")
    JATO  = JatoFactory.get_jato("impjatoEpson")
    print (f"{JATO.__class__} : {JATO.get_impressoraJato()}")