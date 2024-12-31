from modelos.restaurante import Restaurante

restaurante_italia = Restaurante('Nonda de lucca', 'Italiano')
restaurante_pizza = Restaurante('Tomanik', 'Pizzaria')
restaurante_japa = Restaurante('kyodo', 'Japones')

restaurante_japa.alterar_status()
restaurante_japa.receber_avaliacao('wellington', 10)
restaurante_japa.receber_avaliacao('bruno', 9)
restaurante_japa.receber_avaliacao('robson', 8)

def main():
    Restaurante.lista_restaurante()


if __name__ == '__main__':
    main()
