from abc import ABC, abstractmethod


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando TV...")
        print("Ligado")

    def desligar(self):
        print("Desligando a TV...")
        print("Desligado!")     


controle = ControleTV()
controle.ligar()
controle.desligar()