#O que é para fazer:

#Crie uma tupla com 5 elementos e realize as seguintes operações: <ul><li>1-Imprima na tela o tamanho da tupla;</li><li>2-Crie uma nova tupla que contenha os elementos da tupla original em ordem reversa;</li><li>3-Imprima na tela os elementos da nova tupla separados por ""-"".</li></ul>

tupla = ('2','1','5','4','3')
print(tupla)
print(len(tupla))
nova_tupla = tuple(reversed(tupla))
separador = '-'
juntar = separador.join(nova_tupla)
print(nova_tupla)
print(juntar)