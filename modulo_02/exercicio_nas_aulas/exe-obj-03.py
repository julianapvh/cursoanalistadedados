#O que é para fazer:

#Criar uma classe simples em Python para representar um produto. A classe deve ter dois atributos: "nome" e "preco". Em seguida, criar um objeto dessa classe com o nome "Arroz" e o preço "5.99".

class Produto():
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
objeto = Produto('Arroz',5.99)
print(objeto.nome, objeto.preco)
