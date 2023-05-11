"""Temas: Entrada de dados, Operadores matemáticos, Operadores lógicos, Estruturas condicionais, Python, Saída de dados

Classificação: Iniciante

O que é para fazer:

Um lojista comprou diversos produtos para sua loja e deseja revendê-lo com margem de lucro diferente dependendo do valor; por exemplo, 
ele deseja obter lucro de 45% caso o produto custe menos que R$ 20,00. Porém, caso o produto custe mais que isso, o lucro deve ser de 30%. 
Escreva um programa em Python que ajude esse lojista.

Como Fazer:

Crie uma variável para receber o valor do produto;
Crie uma condição para verificar a condição solicitada;
Dentro da condição, realize o cálculo necessário.
Imprima as informações para o usuário.
"""

valorProduto = float(input('Digite o valor do produto: '))


if valorProduto < 20:
    lucro = valorProduto
    print(f"O produto custa menos que 20,00 e sua margem de lucro vai ser de 45%")
    margem_de_lucro = valorProduto / 100.0 * 4.5
    print(f'Seu lucro é de {margem_de_lucro}')
    
    
if valorProduto == 20:
    lucro = valorProduto
    print(f"O produto custa 20,00 e sua margem de lucro vai ser de 45%")
    margem_de_lucro = valorProduto / 100.0 * 4.5
    print(f'Seu lucro é de {margem_de_lucro}')
    
elif valorProduto > 20:
    lucro = valorProduto
    print(f"O produto custa mais que 20,00 e sua margem de lucro vai ser de 30%")
    margem_de_lucro = valorProduto / 100.0 * 3.0
    print(f'Seu lucro é de {margem_de_lucro}')
