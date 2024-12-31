from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_italia = Restaurante('Nonda de lucca', 'Italiano')
restaurante_pizza = Restaurante('Tomanik', 'Pizzaria')
restaurante_japa = Restaurante('kyodo', 'Japones')

restaurante_japa.alterar_status()
restaurante_japa.receber_avaliacao('wellington', 10)
restaurante_japa.receber_avaliacao('bruno', 9)
restaurante_japa.receber_avaliacao('robson', 8)

prato_1 = Prato('Pipoca', 5.00, 'Pipoca na manteiga')
bebida_1 = Bebida('Coca-Cola', 8.00, 'Grande')

restaurante_japa.adicionar_bebida(bebida_1)
restaurante_japa.adicionar_prato(prato_1)


def main():
    Restaurante.lista_restaurante()
    print(prato_1)
    print(bebida_1)


if __name__ == '__main__':
    main()
