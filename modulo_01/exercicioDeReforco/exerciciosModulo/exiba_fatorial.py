def fatorial(nummero):
    if nummero == 1:
        return 1
    else:
        return nummero * fatorial(nummero - 1)

numero = int(input("Digite um número para calcular o fatorial: "))
resultado = fatorial(numero)

print(resultado)