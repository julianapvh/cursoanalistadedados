'''Temas: Objetos, Python, Funções, Entrada de dados, Saída de dados, Orientação a Objetos, Classes

Classificação: Intermediário

O que é para fazer:

Crie uma classe Retangulo que tenha os atributos base e altura e os métodos area e perimetro. Em seguida, crie um objeto da classe Retangulo, leia os valores de base e altura desse objeto do usuário e exiba na tela a área e o perímetro do retangulo.

Como Fazer:

Crie uma classe chamada Retangulo;
Defina os atributos base e altura da classe Retangulo;
Defina os métodos area e perimetro da classe Retangulo. A fórmula da área é base x altura, e a fórmula do perímetro é 2 x (base + altura);
Crie um objeto da classe Retangulo;
Peça ao usuário para digitar os valores de base e altura do objeto;
Use os métodos area e perimetro para calcular a área e o perímetro do retângulo;
Exiba na tela a área e o perímetro do retângulo.'''


class Retangulo():
    def __init__(self,base, altura):
        self.base = base
        self.altura = altura
        
    def area(self):
        return self.base * self.altura
        
    def perimetro(self):
        return 2 * (self.base + self.altura)
        
        
base = float(input("Digite os valores da base do objeto: "))
altura = float(input("Digite os valores da altura do objeto: "))

retangulo = Retangulo(base, altura)

print(retangulo.area())
print(retangulo.perimetro())

