from modelos.restaurante import Restaurante

restaurante_italia = Restaurante('Nonda de lucca', 'Italiano')
restaurante_pizza = Restaurante('Tomanik', 'Pizzaria')
restaurante_japa = Restaurante('kyodo', 'Japones')

restaurante_japa.alterar_status()

def main():
    Restaurante.lista_restaurante()


if __name__ == '__main__':
    main()
