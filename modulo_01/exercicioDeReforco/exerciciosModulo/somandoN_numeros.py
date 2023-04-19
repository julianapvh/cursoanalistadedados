"""Temas: Entrada de dados, Operadores matemáticos, Estruturas condicionais, Estruturas de repetição, Python, Saída de dados

Classificação: Iniciante

O que é para fazer:

Escreva um programa em Python que some diversos números fornecidos pelo usuário. 
A quantidade de números que serão somados, também deve ser fornecida pelo usuário.

Como Fazer:

Crie uma variável para receber a quantidade de números que serão somados a ser fornecida pelo usuário;
Crie um laço para percorrer a quantidade de vezes que o usuário informa a variável anterior;
Crie as variáveis de número e soma;
Realize o cálculo necessário;
Imprima a informação para o usuário."""


quantidade = int(input("Quantos números você quer somar? "))

soma = 0
for i in range(quantidade):
    numero = float(input("Digite o número {}: ".format(i+1)))
    soma += numero
print("A soma dos {} números digitados é igual a {:.2f}.".format(quantidade, soma))






    

