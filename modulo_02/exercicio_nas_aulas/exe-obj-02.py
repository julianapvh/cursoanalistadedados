#O que é para fazer:

#Crie uma classe simples em Python para representar um animal. A classe deve ter um atributo "nome" e um método "falar", que exibe uma mensagem na tela com o som que o animal faz.

class Animal():
    def __init__(self):
        self.nome = 'faisca'
        
    def falar(self):
        print('auau')
    
    def set_nome(self,nome):
        self.nome = nome 
    
    def get_nome(self):
        print (self.nome)
    
animal = Animal()
animal.get_nome()
animal.set_nome('Fumaça faz')
animal.get_nome()
animal.falar()

