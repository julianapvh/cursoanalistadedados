# Define as opções de atendimento e suas sub-opções
opcoes = {
    '1': {
        'texto': 'Dúvidas',
        'sub_opcoes': {
            '1': 'Como faço para me cadastrar?',
            '2': 'Qual o prazo de entrega dos produtos?',
            '3': 'Como alterar minha senha?',
        }
    },
    '2': {
        'texto': 'Consultas',
        'sub_opcoes': {
            '1': 'Verificar status de um pedido',
            '2': 'Solicitar informações sobre um produto',
            '3': 'Saber sobre promoções',
        }
    },
    '3': {
        'texto': 'Informações',
        'sub_opcoes': {
            '1': 'Conhecer mais sobre a empresa',
            '2': 'Saber sobre a política de privacidade',
            '3': 'Obter informações de contato',
        }
    },
    '4': {
        'texto': 'Sair',
    }
}

# Inicia o atendimento
print('Bem-vindo ao nosso atendimento automatizado! Como podemos ajudar?')
opcao = ''

# Repete enquanto o usuário não escolher a opção de sair
while opcao != '4':
    # Mostra as opções disponíveis
    for chave, valor in opcoes.items():
        print(chave, '-', valor['texto'])
    # Pede para o usuário escolher uma opção
    opcao = input('Digite o número da opção desejada: ')
    # Verifica se a opção é válida
    if opcao not in opcoes:
        print('Opção inválida, por favor escolha novamente.')
        continue
    # Verifica se a opção é para sair
    if opcao == '4':
        print('Atendimento encerrado.')
        break
    # Mostra as sub-opções da opção escolhida
    sub_opcoes = opcoes[opcao]['sub_opcoes']
    for chave, valor in sub_opcoes.items():
        print(chave, '-', valor)
    # Pede para o usuário escolher uma sub-opção
    sub_opcao = input('Digite o número da opção desejada: ')
    # Verifica se a sub-opção é válida
    if sub_opcao not in sub_opcoes:
        print('Opção inválida, por favor escolha novamente.')
        continue
    # Mostra a resposta correspondente à sub-opção escolhida
    print('Resposta para', sub_opcoes[sub_opcao])
    # Pede para o usuário se deseja reiniciar o atendimento
    reiniciar = input('Deseja fazer uma nova consulta? (s/n): ')
    # Verifica se o usuário deseja reiniciar o atendimento
    if reiniciar.lower() != 's':
        print('Atendimento encerrado.')
        break
