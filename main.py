from CentralPrint import CentralPrint


class Main:
    @staticmethod
    def exec():
        CentralPrint.get_instancia()
        CentralPrint.create()
        x = CentralPrint()
        CentralPrint.show(x)


Main.exec()
