"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""

# Exemplo de string simples
variavel = 'ABC'

# Formatação básica com f-strings
print(f'{variavel}')  # Saída: ABC

# Alinhamento à direita com 10 caracteres de espaço
print(f'{variavel: >10}')  # Saída:        ABC

# Alinhamento à esquerda com 10 caracteres de espaço
print(f'{variavel: <10}.')  # Saída: ABC       .

# Centralização com 10 caracteres de espaço
print(f'{variavel: ^10}.')  # Saída:    ABC    .

# Formatação de números com sinal, separador de milhar e 1 casa decimal
print(f'{1000.4873648123746:0=+10,.1f}')  # Saída: +001,000.5

# Formatação de número inteiro para hexadecimal com 8 dígitos e zeros à esquerda
print(f'O hexadecimal de 1500 é {1500:08X}')  # Saída: O hexadecimal de 1500 é 000005DC

# Conversion flags: !r (repr), !s (str), !a (ascii)
print(f'{variavel!r}')  # Saída: 'ABC' (representação "oficial" da string)
print(f'{variavel!s}')  # Saída: ABC (conversão para string padrão)
print(f'{variavel!a}')  # Saída: 'ABC' (representação ASCII, útil para caracteres especiais)

# Outros exemplos de formatação
numero = 1234.5678
print(f'Número formatado: {numero:0=+10.2f}')  # Saída: Número formatado: +001234.57
print(f'Número em hexadecimal: {255:04x}')  # Saída: Número em hexadecimal: 00ff