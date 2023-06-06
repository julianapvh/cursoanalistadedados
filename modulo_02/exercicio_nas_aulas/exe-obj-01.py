#O que é para fazer:

#Crie uma fila de espera com os nomes de cinco pessoas e execute as seguintes operações: <ul><li>1-Imprima na tela a fila atual.</li><li>2-Remova o primeiro elemento da fila e imprima na tela a fila atualizada.</li><li>3-Adicione mais dois nomes à fila e imprima na tela a fila atualizada.</li></ul>

class Pessoas():
    def __init__(self):
        self.lista01 = ['joao','ana','luiz','jose','marcos']

    def get_lista01(self):
        print(self.lista01)
    
    def set_lista01(self):
        self.lista01.pop(0)
    
    def set_lista(self,adicionar):        
        self.lista01.append(adicionar)
    
pessoa = Pessoas()
pessoa.get_lista01()
pessoa.set_lista01()
pessoa.get_lista01()
pessoa.set_lista('mariana')
pessoa.set_lista('leandro')
pessoa.get_lista01()
    