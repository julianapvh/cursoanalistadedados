class Funcionario():
    def __init__ (self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base
        
    def calcularSalario(self):
        pass
        

class FuncCLT(Funcionario):
    def tempo_de_empresa(self, tempo):
        self.tempo = tempo
        
    def calcularSalario(self):
        return self.salario_base * (self.tempo / 100)

class FuncPJ(Funcionario):
    def experiencia (self,experiencia):
        self.experiencia = experiencia

    def calcularSalario(self):
        return self.salario_base * self.experiencia

funcionarioCLT1 = FuncCLT('Fernando', 1300)
funcionarioCLT1.tempo = 12
funcionarioCLT1.calcularSalario()

print (f'O salario do funcionario {funcionarioCLT1.nome} é R${funcionarioCLT1.calcularSalario():.2f}')

funcionarioPJ1 = FuncPJ('Josean', 1300)
funcionarioPJ1.experiencia = 2
funcionarioPJ1.calcularSalario()

print (f'O salario do funcionario {funcionarioPJ1.nome} é R${funcionarioPJ1.calcularSalario():.2f}')




