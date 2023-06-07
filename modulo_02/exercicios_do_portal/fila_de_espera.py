'''Temas: Python, Saída de dados, Listas, Estruturas de repetição

Classificação: Intermediário

O que é para fazer:

Crie uma fila de espera com os nomes de cinco pessoas e execute as seguintes operações: 1-Imprima na tela a fila atual. 2-Remova o primeiro elemento da fila e imprima na tela a fila atualizada. 3-Adicione mais dois nomes à fila e imprima na tela a fila atualizada.

Como Fazer:

Crie uma lista com cinco nomes de pessoas, que representará a fila de espera;
Utilize a função print() para imprimir na tela a fila atual;
Utilize o método pop(0) para remover o primeiro elemento da lista;
Utilize novamente a função print() para imprimir a fila atualizada;
Utilize o método append() para adicionar dois novos nomes à lista;
Novamente, utilize a função print() para imprimir a fila atualizada.'''




fila_de_espera = ['pessoa1', 'pessoa2', 'pessoa3', 'pessoa4', 'pessoa5']
print(fila_de_espera)

fila_de_espera.pop((0))
print(fila_de_espera)

fila_de_espera.extend(['pessoa6', 'pessoa7'])
print(fila_de_espera)