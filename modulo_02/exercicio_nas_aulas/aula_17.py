# abre o arquivo em modo "append"

'''salvar = open('teste.txt', 'a')
salvar.write('Ola mundo\n')
salvar.close()'''

import datetime


class Categoria():
    def __init__(self,titulo):
        self.titulo = titulo
        
class Eventos(Categoria):
    def __init__(self,titulo, data, categoria):
        self.titulo = titulo
        self.data = data
        self.categoria = categoria
        
class Log(Eventos):
    def __init__(self):
        self.eventos = []
        
    def adicionar_eventos(self, evento):
        self.eventos.append(evento)
    def exibir_categorias(self):
    
        print('Categorias disponiveis: ')
        temp = []
        for evento in self.eventos:
            temp.append(evento.categoria.titulo)
            print(evento.categoria.titulo)
            print(temp, "teste")
        file = open("arquivo.txt","a")
        file.write()
        file.close()
        
    evento1 = Eventos('Show1', '06/06/2023')
    evento2 = Eventos('Show2', '07/06/2023')
    evento3 = Eventos('Show3', '08/06/2023')


log.adionar_eventos(evento1, evento2, evento3)
log.exibir_categorias()
log.salvar_em_arquivo('log.txt')

            



