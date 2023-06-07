# O que é para fazer:

#Crie uma classe Retangulo que tenha os atributos base e altura e os métodos area e perimetro. Em seguida, crie um objeto da classe Retangulo, leia os valores de base e altura desse objeto do usuário e exiba na tela a área e o perímetro do retangulo.

class Retangulo():
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        calculo1 = self.base * self.altura
        print(calculo1)
    
    def perimetro(self):
        calculo2 = (self.base + self.altura) * 2
        print(calculo2)
        
calculo = Retangulo(3,5)
calculo.area()
calculo.perimetro() 