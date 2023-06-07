import queue

#fila

'''fila = [10,20,30,40,50]
fila.append(60)
print(fila)

fila.pop(0)
print(fila)

fila.append(70)
fila.pop(0)
print(fila)'''


#------------------------- Exercicio ---------------------------------------
'''Estamos recebendo uma série de strings que
armazenam as respostas de um questionário,
precisamos tratar e armazenar em nosso banco de
dados essas informações. Considerando que
recebemos as informações muito mais rápido do
que tratamos, precisamos utilizar alguma estrutura
para garantir que não vamos perder nada.
1. Qual seria a melhor opção? Uma fila? Uma
pilha?
2. Criar uma classe que vai implementar a
solução para esse problema.'''

'''class Questionario():
    def __init__(self,respostas):
        self.respostas = respostas
        
    def adicionar_fila(self,resposta):
        return self.respostas.append(resposta)
        
questionario = Questionario()
questionario.adicionar_fila('Questão 01')
print(questionario)
        
fila = queue()
fila.put()
fila.put(1)
fila.put(2)
fila.put(3)
print(fila.get())'''

'''Estamos recebendo uma lista de comandos
que os usuários executam no terminal e vamos
gravar essa informação para implementar um
desfazer / refazer. Precisamos armazenar cada
um dos comandos que serão enviados e
controlar esses itens.
1. Qual a melhor estrutura? Pensem no
funcionamento do CTRL+Z como exemplo.
2. Vocês devem implementar essa classe que
vai armazenar os comandos e ter as duas
funções - desfazer / refazer'''

class Armazenar_comandos():
    def __init__(self):
        self.fazer = []
       

    def fazer(self,fazer,x):
        return self.fazer.append(x)
        
    def desfazer(self,desfazer,y):
        temp = self.fazer()
        self.fazer.clear()
        return temp
        
armazenar = Armazenar_comandos()
armazenar.fazer = ['teste','teste2']

remover = Armazenar_comandos()
remover.desfazer = []
print(armazenar.fazer)
print(armazenar.desfazer)



    