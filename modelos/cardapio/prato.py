# Quando eu coloco Prato(ItemCardapio), estou dizendo que a classe prato é filha da classe item cardapio, logo a primeira vai herdar caracteristicas da segunda
# Para utilizar os atributos da classe mãe, utilizamos o parametro a classe super() logo pais chamamos o atributo pricipal da classe mãe,assim ficara super().__init__(atriutos)
# HERANÇA - ISSSO FACILITA A ORGANIZAR JA QUE PODEMOS TER CLASSES BASEADAS EM UMA SÓ ASSIM MANTENDO O PADRAO

from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao
    
    def __str__(self):
        return self._nome
    
    def aplica_desconto(self):
        self._preco -= (self._preco * 0.08) 