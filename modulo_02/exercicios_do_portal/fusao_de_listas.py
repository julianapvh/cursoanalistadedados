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