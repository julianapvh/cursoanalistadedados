mesagem = ''
while(mesagem != 'sair'):
    mesagem = input('Digite uma mensagem ')
    print(mesagem)
    
    
    num = 0.976
    print(f'1: Numero = {num}')
    print('2: Numero = %.3f' % num)
    
  #---and and--------------and and-------and and------------and and-----------and and--------------------------------  
    idade = 23
    while(idade>15 and idade<30):
        print('Você precisa ser maior de 30 ou menor que 15 para sair do loop'
        idade = int(input('Digite sua idade '))
              
              print('Obrigada!')
              
#----------or ----or-------or ----or--------or ----or--------=======-or ----or----=======-or ----or----========================================================


dia = 'terça'

while(dia == 'terça' or dia == 'quarta'):
    print('Você precisa escolher um dia diferente de terça ou quarta para sair do loop')
    dia = input('Que dia é hoje? ')
                print('Obrigada!!!')