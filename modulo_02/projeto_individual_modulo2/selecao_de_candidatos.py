# função para buscar candidatos

def busca_candidatos(candidatos, minimo_entrevista, minimo_teste_teorico, minimo_teste_pratico, minimo_soft_skills):
    candidatos_encontrados = []
    for candidato in candidatos:
        if (candidato['entrevista'] >= minimo_entrevista
            and candidato['teste teórico'] >= minimo_teste_teorico
            and candidato['teste prático'] >= minimo_teste_pratico
            and candidato['soft skills'] >= minimo_soft_skills):
            candidatos_encontrados.append(candidato['Candidato'])
    return candidatos_encontrados

# Lista de com dados de entrevista com candidatos

candidatos = [
    {'Candidato': 1, 'entrevista': 5, 'teste teórico': 10, 'teste prático': 8, 'soft skills': 8},
    {'Candidato': 2, 'entrevista': 10, 'teste teórico': 7, 'teste prático': 7, 'soft skills': 8},
    {'Candidato': 3, 'entrevista': 8, 'teste teórico': 5, 'teste prático': 4, 'soft skills': 9},
    {'Candidato': 4, 'entrevista': 2, 'teste teórico': 2, 'teste prático': 2, 'soft skills': 1},
    {'Candidato': 5, 'entrevista': 10, 'teste teórico': 10, 'teste prático': 8, 'soft skills': 9}
]

# Entrada do usuário, o usuário vai digitar a quantidade minima de nota que ele quer

minimo_entrevista = int(input("Digite a nota mínima para a entrevista: "))
minimo_teste_teorico = int(input("Digite a nota mínima para o teste teórico: "))
minimo_teste_pratico = int(input("Digite a nota mínima para o teste prático: "))
minimo_soft_skills = int(input("Digite a nota mínima para a avaliação de soft skills: "))

# Busca por candidatos que satisfazem os requisitos

candidatos_encontrados = busca_candidatos(candidatos, minimo_entrevista, minimo_teste_teorico, minimo_teste_pratico, minimo_soft_skills)

# Exibição dos candidatos encontrados

if len(candidatos_encontrados) > 0:
    print('Candidatos encontrados na busca:', candidatos_encontrados)
else:
    print('Nenhum candidato encontrado na busca.')