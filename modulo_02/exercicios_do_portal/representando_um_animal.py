'''Temas: Classes, Objetos, Python, Saída de dados, Orientação a Objetos

Classificação: Iniciante

O que é para fazer:

Crie uma classe simples em Python para representar um animal. A classe deve ter um atributo "nome" e um método "falar", que exibe uma mensagem na tela com o som que o animal faz.

Como Fazer:

Crie um novo arquivo em Python chamado "animal.py";
Defina a classe "Animal" com um método construtor init que recebe um parâmetro "nome" e armazena esse valor em um atributo da classe com o mesmo nome;
Crie um método "falar" na classe "Animal" que exibe uma mensagem na tela com o som que o animal faz. Por exemplo, o método poderia exibir a mensagem "O faz "miau" para um gato com nome "Garfield";
Crie um objeto "animal" a partir da classe "Animal" e defina um nome para ele;
Chame o método "falar" do objeto "animal" criado para exibir a mensagem com o som do animal.'''


class Animal():
    def __init__(self, nome):
        self.nome = nome
        
    def falar(self):   
        print(f"O animal {self.nome} faz miau.")

animal = Animal('Garfield')
animal.falar()
        
    
    
    