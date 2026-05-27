class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = int(idade)
    
    def emitir_som(self):
        return "O animal emitiu um som genérico."


class Cachorro(Animal):
    def emitir_som(self):
        return "O cachorro latiu!"
    
class Gato(Animal):
    def emitir_som(self):
        return "O gato miou!"

    

cachorro = Cachorro("Tobi", 5)
gato = Gato("Breninho", 3)
print(gato.emitir_som())
print(cachorro.emitir_som())