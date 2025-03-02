"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

# Exemplo de interpolação de strings com %

# Dados iniciais
nome = 'Luiz'
preco = 1000.95897643

# Interpolação básica
variavel = '%s, o preço é R$%.2f' % (nome, preco)  # %s para string, %.2f para float com 2 casas decimais
print(variavel)

# Exemplo de formatação de inteiro e hexadecimal
numero = 1500
print('O hexadecimal de %d é %08X' % (numero, numero))  # %d para inteiro, %08X para hexadecimal com 8 dígitos e zeros à esquerda

# Outros exemplos de interpolação
idade = 25
altura = 1.75
print('%s tem %d anos e mede %.2f metros.' % (nome, idade, altura))

# Exemplo com hexadecimal minúsculo
print('O hexadecimal de %d em minúsculo é %08x' % (numero, numero))  # %x para hexadecimal minúsculo

# Exemplo com formatação de números grandes
valor_grande = 1_000_000
print('Valor formatado: R$%d' % valor_grande)  # %d para inteiros grandes