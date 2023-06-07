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



'''class Professor(Aluno):
  def __init__(self, formacao, turma):
    self.formacao = formacao
    self.turma = turma
    
  Professor = input('insira o nome do professor: ')
  idade = input('insira a idade do professor: ')
  matricula = input('insira o número da maricula do professor: ')
  professor = Professor(Professor, nome, idade, matricula)
  print(professor.nome, professor.idade, professor.matricula)'''
