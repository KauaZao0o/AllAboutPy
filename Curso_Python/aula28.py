# Solicita ao usuário que digite seu nome e sua idade
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

# Inverte o nome digitado
nome_invertido = nome[::-1]

# Conta a quantidade de caracteres no nome
qtd_letras = len(nome)

# Verifica se os campos nome e idade foram preenchidos
if nome and idade:
    print(f'Seu nome é {nome}')  # Exibe o nome digitado
    print(f'Seu nome invertido é {nome_invertido}')  # Mostra o nome ao contrário

    # Verifica se há espaços no nome
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')

    print(f'Seu nome tem {qtd_letras} letras')  # Mostra a quantidade de caracteres no nome
    
    # Exibe a primeira letra do nome
    print(f'A primeira letra do seu nome é {nome[0]}')

    # Exibe a última letra do nome (acessando a primeira letra do nome invertido)
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    # Caso o usuário não preencha algum campo, exibe uma mensagem de erro
    print('Desculpe, você deixou campos vazios.')