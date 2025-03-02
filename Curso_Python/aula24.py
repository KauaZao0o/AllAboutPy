# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1

# Solicita ao usuário que digite seu nome
nome = input('Digite seu nome: ')

# Solicita ao usuário que digite o que deseja encontrar no nome
encontrar = input('Digite o que deseja encontrar no nome: ')

# Verifica se o texto a ser encontrado está no nome
if encontrar in nome:
    print(f'"{encontrar}" está presente no nome "{nome}".')
else:
    print(f'"{encontrar}" não está presente no nome "{nome}".')

# Adiciona uma verificação adicional para mostrar todas as ocorrências
ocorrencias = nome.count(encontrar)
if ocorrencias > 0:
    print(f'O texto "{encontrar}" aparece {ocorrencias} vez(es) no nome "{nome}".')

# Mostra o nome com as posições dos caracteres
print('\nPosições dos caracteres no nome:')
for indice, letra in enumerate(nome):
    print(f'Posição {indice}: {letra}')

# Verifica se o texto não está no nome usando 'not in'
if encontrar not in nome:
    print(f'\nO texto "{encontrar}" realmente não está no nome "{nome}".')
else:
    print(f'\nO texto "{encontrar}" está presente no nome "{nome}".')