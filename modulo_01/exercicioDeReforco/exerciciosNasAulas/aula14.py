'''def soma (valor1, valor2):
    return valor1 + valor2

def calculaDobroDaSoma(var1, var2):
    resultado = soma(var1, var2)
    dobro = resultado * 2
    return dobro
    
print(calculaDobroDaSoma(var1 = 10, var2 = 20))'''

#=======================Exercicio=================================================

'''criar uma nova função que será utilizada dentro do retorno da função calculaDobroDaSoma
e essa função deve imprimir o resultado da seguinte forma:
'A soma do valor1 mais o valor2 é igual ao resultado e seu dobro é igual ao dobro'''


'''def soma (valor1, valor2):
    return valor1 + valor2

def calculaDobroDaSoma(var1, var2):
    resultado = soma(var1, var2)
    dobro = resultado * 2
    return dobro

def mostrarResultado(valor1, valor2, resultado, dobro):
return
    
 print(f"A soma do {valor1} mais o {valor2} é igual a {resultado} e o seu dobro é igual a {dobro}")'''
 
 
 #============================exemplo do professor ================================================================
''' def soma(valor1, valor2):
    return valor1+ valor2

def imprimir(valor1, valor2, resultado, dobro):
    print(f"A soma do {valor1} mais o {valor2} é igual a {resultado} e o seu dobro é igual a {dobro}")

def calculaDobroDaSoma(valor1, valor2):
    resultado = soma(valor1,valor2)
    dobro = resultado * 2
    return imprimir(valor1, valor2, resultado, dobro)

calculaDobroDaSoma(2,3)'''
    
#============================exemplo do professor ==================================================================
    
def fatorial(numero):
    if numero == 1:
        return 1
    return numero * fatorial(numero - 1)

print(fatorial(3))



    
    
    
