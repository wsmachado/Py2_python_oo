# para criar uma classe no python utilziamos a instancia class nome(), como padrao utilizamo a primira letra da classe maiuscula
# __inti__ garante que quando a classe seja criada as variaveis dadas sejam semore estanciadas
# __str__ caso precise mostra o obejto no formato de texxto, geralmete o espaço da memoria que esta alocado, ele mostra oq vai ser passdo no __str__
# Criar um metodo para listar todos os restaurantes que estao listados nessa classe para isso, criamos isso como se fosse uma def dentro da classse 
class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        # Title() garante que a primeira letra seja maiuscula
        self._nome = nome.title()
        # upper() garante que a palvra seja salva toda em letra maiuscula
        self._categoria = categoria.upper()
        #iremos mudar a forma que o atriuto aixo sera lido, para isso utilizaremos o @propety
        # self.ativo = False
        # Ao colocar o underscore antes do ativo (_ativo), estamos dizendo que ele é um atriuto privado e que n estamos esperando que as pessoas o acessem diretamente (POR CONVENSAO)
        self._ativo = False
        # Toda vez que criar um objeto Restaurante, ira colar ele dentro da lista restaurantes
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self._nome} | {self._categoria}'


    # Sempre que temos um metodo que é referenciado a classe e nao uma instancia, colocamos antes dele um @classmethod (diz que é um atriuto da classe)
    #por convesao colocamos nesse um argumetno cls
    @classmethod
    def lista_restaurante(cls):
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria do Restaurante'.ljust(25)} | Status do Restaurante')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')

    # Sempre que utilizarmos @property, queremos modificar como aquele atributo vai ser lido
    # para funcionar o atriuto ativo deve ser privado, ja que ele n ira ser passado no self pelos clientes, caso contrario apecera o seguinte erro "a propriedade ativo não tem um setter".
    # Emojis https://coolsymbol.com
    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'


    def alterar_status(self):
        self._ativo = not self._ativo


# NAO IREMOS MAIS UTILIZAR ESSA CODIGO PARA ESTANCIAR AS CLASSES CRIAREMOS UM CODIGO APP.PY
# testanto
# restaurante_pizza = Restaurante('Pizzaria', 'Tomanik')
# restaurante_pizza.alterar_status()
# restaurante_pizza.categoria = 'Pizzaria'
# restaurante_pizza.nome = 'Tomanik'
# restaurante_japa = Restaurante('Japones', 'Kyodo')

# Restaurante.lista_restaurante()


# Retorna todos os objetos que existem dentro da classe
# print(dir(restaurante_pizza))

# Retorna um dicionario com os atributos
# print(vars(restaurante_pizza))



