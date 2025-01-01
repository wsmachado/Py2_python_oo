from modelos.avaliacao import Avalicao
from modelos.cardapio.item_cardapio import ItemCardapio

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
        # Receberar uma lista de avalicaoes dos clientes ja que cada objeto pode ter mais de uma avaliaco
        self._avaliacao = []
        self._cardapio = []
        # Toda vez que criar um objeto Restaurante, ira colar ele dentro da lista restaurantes
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self._nome} | {self._categoria}'


    # Sempre que temos um metodo que é referenciado a classe e nao uma instancia, colocamos antes dele um @classmethod (diz que é um atriuto da classe)
    #por convesao colocamos nesse um argumetno cls
    @classmethod
    def lista_restaurante(cls):
        print(f'\n{'Nome do Restaurante'.ljust(25)} | {'Categoria do Restaurante'.ljust(25)} | {'Avaliações'.ljust(25)} | Status do Restaurante')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_notas).ljust(25)} | {restaurante.ativo}')
        print()

    # Sempre que utilizarmos @property, queremos modificar como aquele atributo vai ser lido
    # para funcionar o atriuto ativo deve ser privado, ja que ele n ira ser passado no self pelos clientes, caso contrario apecera o seguinte erro "a propriedade ativo não tem um setter".
    # Emojis https://coolsymbol.com
    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'

    def alterar_status(self):
        self._ativo = not self._ativo

    # metodo que recee as avaliacoes
    def receber_avaliacao(self,  cliente, nota):
        if 0 <= nota <= 5:
            avaliacao = Avalicao(cliente, nota)
            self._avaliacao.append(avaliacao)

    # Criar o @property para calcular a media das avaliacaoes de cada restaurante
    @property
    def media_notas(self):
        if not self._avaliacao:
            return '-'
        
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        qtd_avaliacao = len(self._avaliacao)
        media = round(soma_notas / qtd_avaliacao, 1)

        return media
    

    #Aqui utilizamos a funcao isintance, que basicam verifica se o item que passamos no argumento é uma instancia da classe ItemCardapio
    #Ja que utilizamos ItemCardapio como uma classe mae, o isinstance retornarar verdadeiro tbm para a classe de bebida e comida
    def adicionar_item_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    
    # Criaremos uma propriedade para printar o cardapio, ja que n precisa de nenhuma manipulacao dos dados
    @property
    def mostrar_cardapio(self):
        print(f'\nCardapido do restaurante, {self._nome}:\n')
        # a classe enumerate enumera os itens na lista pssada, no qual abaixo, o i sera o indece e o item o elemento da lista
        for i, item in enumerate(self._cardapio, start=1):
            # a funcao hasattr verifica se um atriuto especifico esta dentro de uma lisa
            if hasattr(item, '_descricao'):
                msg_prato = f'{i}. Nome: {item._nome} | Preço: {item._preco} | Descrição: {item._descricao}'
                print(msg_prato)
            elif hasattr(item, '_tamanho'):
                msg_bebida = f'{i}. Nome: {item._nome} | Preço: {item._preco} | Tamanho: {item._tamanho}'
                print(msg_bebida)
        print()




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



