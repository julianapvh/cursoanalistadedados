'''Temas: Funções, Python, Entrada de dados, Orientação a Objetos, Classes, Objetos, Encapsulamento, Saída de dados

Classificação: Intermediário

O que é para fazer:

Crie uma classe Aluno que tenha os atributos nome, idade e matrícula. Em seguida, crie um objeto da classe Aluno, leia os valores de nome, idade e matrícula desse objeto do usuário e exiba na tela os dados do aluno cadastrado.

Como Fazer:

Crie uma classe chamada Aluno;
Defina os atributos nome, idade e matrícula da classe Aluno;
Crie um objeto da classe Aluno;
Peça ao usuário para digitar os valores de nome, idade e matrícula do objeto;
Exiba na tela os dados do aluno cadastrado.'''


class Aluno():
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
        
nome = input('Digite o nome do aluno: ')
idade = int(input('Digite a idade do aluno: '))
matricula = int(input('Digite a matricula do aluno: '))

aluno = Aluno(nome,idade,matricula)
print(f'Os dados do aluno(a) são: Nome:{nome}, Idade: {idade} anos, Matricula: {matricula}')