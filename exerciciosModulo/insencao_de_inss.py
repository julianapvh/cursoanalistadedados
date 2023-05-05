'''Temas: Entrada de dados, Operadores matemáticos, Estruturas condicionais, Python, Saída de dados

Classificação: Intermediário

O que é para fazer:

Escreva um programa em Python que exiba o desconto do INSS segundo seu salário. Por exemplo, se o usuário possuir salário inferior ou igual a R$: 600,00 ele será isento, em caso de maior que R$: 600,00 e menor ou igual a R$:1.200,00, o desconto é de 20%; em caso de Maior que R$: 1.200,00 e menor ou igual a R$: 2.000,00, o desconto é de 25%; e em caso de maior que R$: 2.000,00, o desconto é de 30%.

Como Fazer:

Crie uma variável para receber o salário do usuário;
Crie uma condição para fazer as verificações necessárias;
Dentro das verificações, crie a variável que vai armazenar o cálculo do desconto;
Imprima o valor do desconto para o usuário.'''


salario = float(input("Digite o seu valor do seu salário: "))

if salario <= 600:
    desconto = 0
elif salario <= 1200:
    desconto = salario * 0.2
elif salario <= 2000:
    desconto = salario * 0.25
else:
    desconto = salario * 0.3

print("O desconto do INSS é de R$ {:.2f}".format(desconto))