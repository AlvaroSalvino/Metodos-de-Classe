from abc import ABC, abstractmethod, abstractproperty


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando TV...")
        print("Ligado")

    def desligar(self):
        print("Desligando a TV...")
        print("Desligado!")

    @property
    def marca(self):
        return "LG"

class ControleArCondicionado(ControleRemoto):
    def ligar(self):   
        print("Ligando Ar...")
        print("Ligado")

    def desligar(self):
        print("Desligando a Ar...")
        print("Desligado!")

    @property
    def marca(self):
        return "philco"


controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)


controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)