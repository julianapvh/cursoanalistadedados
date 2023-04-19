sentenca = 'Está é uma string'
#print(len(sentenca))
#for i in range(len(sentenca)):
    #print(sentenca[i])
    
    # () função
    # [] indice - posição - sumário
    # {} lista / tupla
print(sentenca[0:10])

#trocar
nova_sentenca = 'Aquela' + sentenca[5:]
print(nova_sentenca)

#replace - trocar
print(sentenca.replace('', '*'))

#lower - deixar minusculo
print(sentenca.lower())

#upper - deixar maiusculo
print(sentenca.upper())

#find - substituir
indice = sentenca.find('uma')
print(indice)