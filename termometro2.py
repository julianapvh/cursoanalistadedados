temperatura = float(input('Qual é a sua temperatura?'))

while(str(temperatura) != 'sair'):

 if (str(temperatura) <= 37):
    print("Nada de febre!")
 
else:
    print('Você está com febre')