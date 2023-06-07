'''Temas: Entrada de dados, Objetos, Classes, Orientação a Objetos, Saída de dados, Funções, Operadores matemáticos, Python

Classificação: Iniciante

O que é para fazer:

Criar uma classe simples em Python para representar um produto. A classe deve ter dois atributos: "nome" e "preco". Em seguida, criar um objeto dessa classe com o nome "Arroz" e o preço "5.99".

Como Fazer:

Crie um novo arquivo em Python chamado ""produto.py"";
Defina a classe ""Produto"" com um método construtor init que recebe dois parâmetros: ""nome"" e ""preco"", e armazena esses valores em atributos da classe com os mesmos nomes;
Crie um objeto ""arroz"" a partir da classe ""Produto"" com o nome ""Arroz"" e o preço ""5.99"";
Exiba o nome e o preço do objeto ""arroz"" na tela.'''


class Produto():
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
arroz = Produto('Arroz', 5.99)

print(arroz.nome, arroz.preco)
