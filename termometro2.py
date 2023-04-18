temperatura = float(input('Qual é a sua temperatura?'))
while(temperatura != 'sair'):

 if (temperatura <= 37):
    print("Nada de febre!")
 
else:
    print('Você está com febre')