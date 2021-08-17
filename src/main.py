from CentralPrint import CentralPrint


class Main:
    @staticmethod
    def init():
        CentralPrint.get_instancia()
        CentralPrint.create()
        CentralPrint.show(CentralPrint())


Main.init()
