'''nomes = ['Rafael', 'Will', 'Marina', 'Miguel', 'Cesar']
print(nomes[1:3])'''


'''nomes = ['Rafael', 'Will', 'Marina', 'Miguel', 'Cesar']

lista_copia = nomes[:]

lista_copia[1] = 'Univitelinas'

print(nomes)
lista_copia.sort() # ordem decrecente (reverse = True)

print(lista_copia)'''




#exercises  01
'''pizzas = ['Calabresa', 'Mussarela', 'Marguerita']

pizza_do_amigo = pizzas[:]

pizza_do_amigo.append('Escarola')
pizza_do_amigo.insert(2,'Portuguesa')

print('Minhas pizzas favoritas são: '+ str(pizzas))
print('As pizzas favoritas do meu amigo são: '+ str(pizza_do_amigo))'''



'''frutas = ['Maçã', 'Figo', 'Banana', 'Pessego', 'Melancia', 'Mamão','Kiwi']

#nova_lista = [i for i in frutas if 'a' not in i]

#for i in frutas:
    # if 'a' not in i:
          #nova_lista.append(i)
maiuscula = [i.upper() for i in frutas]

print(maiuscula)'''



'''quadrados = [valor**2 for valor in range(1,10)]
             
print(quadrados)'''


# exercicio 02

lista_cubos = [valor**3 for valor in range(1,20,2)]

print(lista_cubos)