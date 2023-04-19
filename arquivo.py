aluno = input("Nome do aluno: ").upper()

nota1 = float(input(f"Insira a nota 1 do(a) aluno(a) {aluno}: "))
nota2 = float(input(f"Insira a nota 2 do(a) aluno(a) {aluno}: "))
nota3 = float(input(f"Insira a nota 3 do(a) aluno(a) {aluno}: "))

media = nota1 + nota2 + nota3 / 3 
aproveitamento = (nota1 + nota2 * 2 + nota3 * 3 + media) / 7

if aproveitamento >= 9.0:
    print(f"O aluno(a) {aluno} foi APROVADO com conceito A")
    
elif aproveitamento >= 7.5 and aproveitamento < 9.0:
    print(f"O aluno(a) {aluno} foi APROVADO com conceito B")    
    
elif aproveitamento >= 6.0 and aproveitamento < 7.5:
    print(f"O aluno(a) {aluno} foi APROVADO com conceito C")
    
elif aproveitamento >= 4.0 and aproveitamento < 6.0:
    print(f"O aluno(a) {aluno} foi REPROVADO com conceito D")
    
elif aproveitamento < 4.0:
    print(f"O aluno(a) {aluno} foi REPROVADO com conceito E")