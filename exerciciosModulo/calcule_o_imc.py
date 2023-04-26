'''Temas: Entrada de dados, Operadores matemáticos, Estruturas de repetição, Python, Saída de dados

Classificação: Intermediário

O que é para fazer:

Escreva uma programa em Python que peça a quantidade de pacientes e calcule o IMC a partir do nome, peso e altura para cada um deles.

Como Fazer:

Crie uma variável que vai armazenar o número de pacientes;
Crie um for para percorrer a quantidade de pacientes;
Crie variáveis para armazenar nome, altura e peso;
Crie uma variável para calcular o IMC e faça o cálculo necessário;
Imprima os dados na tela.'''

quantidade_pacientes = int(input('Digite a quantidade de pacientes: '))


for i in range(quantidade_pacientes):
    nome_paciente = input('Digite o nome do(a) paciente: ')
    altura_paciente = float(input('Digite a altura do(a) paciente (em metros): '))
    peso_paciente = float(input('Digite o peso do(a) paciente em kg: '))
    
    imc = peso_paciente / (altura_paciente * altura_paciente)
    
    
    print('\nNome do(a) paciente: ', nome_paciente)
    print('\naltura do(a) paciente: ', altura_paciente, 'm')
    print('\nPeso do(a) paciente: ', peso_paciente, 'kg: ')
    print('O IMC do(a) paciente ' + str(nome_paciente) + ' é: {:.2f}' .format(imc))
    


          
          
          
    
    
