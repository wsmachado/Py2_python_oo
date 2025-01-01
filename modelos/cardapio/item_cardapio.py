from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    # Cria um monde para as classes derivadas teem obrigatoriamente um metodo para desconto do cardapio
    # como é o metodo abstrato em cada class filha dessa que temos, podemos colocar regras diferentes

    @abstractmethod
    def aplica_desconto(self):
        pass
