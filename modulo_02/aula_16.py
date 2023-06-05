class Funcionario():
    def __init__(self,nome, salario_base,calcular_salario):
    
     self.nome = ""
     self.salario_base = ""
     self.calcular_salario = ""
    def get_nome(self):
        print(self.nome)
        
    def get_salario_base(self):
        return self.salario_base
        
    def get_calcular_salario(self):
        return self.calcular_salario
        
    
    
    
    
class Funcionario_clt(Funcionario):
    def __init__(self,tempo_de_empresa):
     self.tempo_de_empresa = tempo_de_empresa
     return (self.get_salario_base * self.tempo_de_empresa) /100
     

class Funcionario_pj(Funcionario):
    def __init__(self,experiencia,):
     self.experiencia =experiencia
     return self.get_salario_base * self.experiencia
     
     
    salario = Funcionario('João', 10, 5)
    print(salario)




