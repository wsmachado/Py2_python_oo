from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_italia = Restaurante('Nonda de lucca', 'Italiano')
restaurante_pizza = Restaurante('Tomanik', 'Pizzaria')
restaurante_japa = Restaurante('kyodo', 'Japones')

restaurante_japa.alterar_status()
restaurante_japa.receber_avaliacao('wellington', 4)
restaurante_japa.receber_avaliacao('bruno', 3)
restaurante_japa.receber_avaliacao('robson', 5)

prato_1 = Prato('Pipoca', 5.00, 'Pipoca na manteiga')
prato_1.aplica_desconto()
bebida_1 = Bebida('Coca-Cola', 8.00, 'Grande')
bebida_1.aplica_desconto()
bebida_2 = Bebida('Monster', 8.00, 'Mêdio')

restaurante_japa.adicionar_item_cardapio(bebida_1)
restaurante_japa.adicionar_item_cardapio(prato_1)
restaurante_japa.adicionar_item_cardapio(bebida_2)


def main():
    # Restaurante.lista_restaurante()
    restaurante_japa.mostrar_cardapio


if __name__ == '__main__':
    main()
