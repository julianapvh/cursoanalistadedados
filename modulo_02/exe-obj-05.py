# O que é para fazer:

#Crie uma classe Aluno que tenha os atributos nome, idade e matrícula. Em seguida, crie um objeto da classe Aluno, leia os valores de nome, idade e matrícula desse objeto do usuário e exiba na tela os dados do aluno cadastrado.

class Aluno():
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula

nome = input('insira o nome: ')    
idade = input('insira a idade: ')
matricula = input('insira o numero da matricula: ')
aluno = Aluno(nome,idade,matricula)
print(aluno.nome, aluno.idade, aluno.matricula)    