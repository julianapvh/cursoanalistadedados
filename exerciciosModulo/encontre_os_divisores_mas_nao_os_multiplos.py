"""Temas: Entrada de dados, Saída de dados, Funções, Listas, Operadores matemáticos, Estruturas condicionais, Estruturas de repetição, Python

Classificação: Intermediário

O que é para fazer:

Escreva um programa que encontrará todos esses números que são divisíveis por 7, 
mas não são um múltiplo de 5, entre 2000 e 3200 (ambos incluídos).

Como Fazer:

Crie uma lista para armazenar os números;
Crie um laço para percorrer o processo no intervalo solicitado;
Crie uma condição para verificar o que foi solicitado;
Adicione os resultados na lista criada anteriormente;
Imprima os valores para o usuário."""


# Criando a lista para armazenar os números
numeros = []

# Loop para percorrer o intervalo solicitado
for i in range(2000, 3200):
    # Condição para verificar se o número é divisível por 7 e não é múltiplo de 5
    if i % 7 == 0 and i % 5 != 0:
        # Adicionando o número na lista
        numeros.append(i)

# Imprimindo os valores para o usuário
print("Os números divisíveis por 7, mas não múltiplos de 5, entre 2000 e 3200 são:")
print(numeros)