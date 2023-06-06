'''Temas: Listas, Python, Saída de dados

Classificação: Intermediário

O que é para fazer:

Crie duas listas de tamanho igual com valores numéricos de sua escolha. Crie uma nova lista que seja a fusão das duas primeiras, de forma que os elementos sejam intercalados. Por fim, imprima a nova lista na tela.

Como Fazer:

Crie duas listas de tamanho igual com valores numéricos de sua escolha;
Crie uma nova lista vazia para armazenar a fusão das duas primeiras;
Utilize um laço de repetição para percorrer todos os índices das listas originais;
Para cada índice, adicione o elemento da primeira lista na nova lista e, em seguida, adicione o elemento correspondente da segunda lista na nova lista;
Se as listas originais possuem tamanhos diferentes, adicione os elementos restantes da lista maior no final da nova lista;
Imprima a nova lista na tela.'''


lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]

nova_lista = []

tamanho = len(lista1)  # Considerando que as duas listas têm o mesmo tamanho

for i in range(tamanho):
    nova_lista.append(lista1[i])
    nova_lista.append(lista2[i])

# Se as listas tiverem tamanhos diferentes, adicionamos os elementos restantes da lista maior
if len(lista1) > len(lista2):
    nova_lista.extend(lista1[tamanho:])
else:
    nova_lista.extend(lista2[tamanho:])

print(nova_lista)