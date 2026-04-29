class Cliente:
    def __init__(self, n, fone):
        self._nome = n
        self._telefone = fone
#A palavra reservada pass é usada para indicar que o corpo da classe está vazio, ou seja, não há atributos ou métodos definidos
#__init__ é um método especial em Python que é chamado automaticamente quando um objeto da classe é criado. Ele é usado para inicializar os atributos do objeto. No exemplo acima, o método __init__ não está fazendo nada, mas ele pode ser modificado para incluir atributos e lógica de inicialização conforme necessário.
#self é uma referência ao próprio objeto que está sendo criado. Ele é usado para acessar os atributos e métodos da classe dentro do método __init__ ou de outros métodos da classe.
#Com o parâmetro self são passados os parâmetros que serão utilizados para inicialização dos atributos
#método get
def  get_nome(self):
    return self._nome
#método set
def set_nome(self,nome):
    self._nome=nome