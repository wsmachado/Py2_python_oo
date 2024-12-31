# Quando eu coloco Prato(ItemCardapio), estou dizendo que a classe prato é filha da classe item cardapio, logo a primeira vai herdar caracteristicas da segunda
# Para utilizar os atributos da classe mãe, utilizamos o parametro a classe super() logo pais chamamos o atributo pricipal da classe mãe,assim ficara super().__init__(atriutos)
# HERANÇA - ISSSO FACILITA A ORGANIZAR JA QUE PODEMOS TER CLASSES BASEADAS EM UMA SÓ ASSIM MANTENDO O PADRAO

from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self._tamanho = tamanho
    
    def __str__(self):
        return self._nome