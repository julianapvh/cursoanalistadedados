"""➔ O QUE FAZER?
Criar um novo arquivo .py.
1. Escreva um loop que inicia no último caractere da string e caminha para o primeiro caractere,
imprimindo cada letra em uma linha separada.
2. Dado que a variável sentenca é uma string, qual o resultado de sentenca[:]?
3. Teste alterar o valor de um caractere de uma string"""

sentenca = 'Loop da aula onze'
                            #[::-1] outra forma de fazer
for i in range(len(sentenca)-1, -1, -1):
    print(sentenca[i])
print(len(sentenca))
print(sentenca)


