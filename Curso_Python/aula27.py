"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""

# Exemplo de string
variavel = 'Olá mundo'

# Fatiamento básico
print('String original:', variavel)

# Fatiamento para inverter a string
print('String invertida:', variavel[::-1])  # [::-1] inverte a string

# Fatiamento para pegar parte da string
print('Do índice 0 ao 3:', variavel[0:3])  # Pega do índice 0 ao 2 (3 não incluso)
print('Do índice 4 ao final:', variavel[4:])  # Pega do índice 4 até o final
print('Do início ao índice 6:', variavel[:6])  # Pega do início até o índice 5 (6 não incluso)

# Fatiamento com passo (p)
print('De 2 em 2 caracteres:', variavel[::2])  # Pega os caracteres de 2 em 2
print('De trás para frente com passo 1:', variavel[::-1])  # Inverte a string
print('De trás para frente com passo 2:', variavel[::-2])  # Inverte a string e pega de 2 em 2

# Usando índices negativos
print('Último caractere:', variavel[-1])  # Último caractere
print('Do índice -5 ao -1:', variavel[-5:-1])  # Pega do índice -5 ao -2

# Função len para contar caracteres
print('Quantidade de caracteres:', len(variavel))  # Retorna o tamanho da string