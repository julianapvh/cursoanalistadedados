
tomateSemanaAnterior = float(input('Quanto você pagou pelo tomate na semana passada?'))
tomateSemanaAtual = float(input('Quanto você pagou pelo tomate na semana atual?'))
alimentos = 'tomate', 'laranja', 'abacaxi', 'limao'





resultadoTomate = tomateSemanaAnterior - tomateSemanaAtual

if (resultadoTomate == 0 ):
    print("O preço do tomate não sofreu alteração")

elif (resultadoTomate < 0 ):
    print(f"O tomate aumentou R$ {resultadoTomate * (-1):,.2f}  reais")
    
else:
    
    print(f'O preço do tomate diminuiu R$ {resultadoTomate:,.2f} reais')
    
    # calculo da laranja
    
    laranjaSemanaAnterior = float(input('Quanto você pagou pela laranja na semana passada?'))
laranjaSemanaAtual = float(input('Quanto você pagou pela laranja na semana atual?'))


resultadoLaranja = laranjaSemanaAnterior - laranjaSemanaAtual

if (resultadoLaranja == 0 ):
    print("O preço da laranja não sofreu alteração")

elif (resultadoLaranja < 0 ):
    print(f"A laranja aumentou R$ {resultadoLaranja * (-1):,.2f}  reais")
    
else:
    
    print(f'A laranja diminuiu R$ {resultadoLaranja:,.2f} reais')
    
    # calculo do abacaxi
    
    abacaxiSemanaAnterior = float(input('Quanto você pagou pelo abacaxi na semana passada?'))
abacaxiSemanaAtual = float(input('Quanto você pagou pelo abacaxi na semana atual?'))


resultadoAbacaxi = abacaxiSemanaAnterior - abacaxiSemanaAtual

if (resultadoAbacaxi == 0 ):
    print("O preço do abacaxi não sofreu alteração")

elif (resultadoAbacaxi < 0 ):
    print(f"O abacaxi aumentou R$ {resultadoAbacaxi * (-1):,.2f}  reais")
    
else:
    
    print(f'O abacaxi diminuiu R$ {resultadoAbacaxi:,.2f} reais')
    
    # calculo do limão
    
    
limaoSemanaAnterior = float(input('Quanto você pagou pelo limão na semana passada?'))
limaoSemanaAtual = float(input('Quanto você pagou pelo limão na semana atual?'))


resultadoLimao = limaoSemanaAnterior - limaoSemanaAtual

if (resultadoLimao == 0 ):
    print("O preço do limão não sofreu alteração")

elif (resultadoLimao < 0 ):
    print(f"O limão aumentou R$ {resultadoLimao * (-1):,.2f}  reais")
    
else:
    
    print(f'O limão diminuiu R$ {resultadoLimao:,.2f} reais')