"""
Introdução ao try/except
try -> Tenta executar o código dentro do bloco
except -> Captura um erro caso ocorra durante a execução do try
"""

# Solicita ao usuário que digite um número
numero_str = input('Vou dobrar o número que você digitar: ')

try:
    # Tenta converter a string para float
    numero_float = float(numero_str)
    
    # Exibe o número convertido e o dobro dele
    print(f'FLOAT: {numero_float}')
    print(f'O dobro de {numero_float} é {numero_float * 2:.2f}')
except ValueError:
    # Captura erro caso a conversão falhe (exemplo: entrada inválida como "abc")
    print('Erro: Isso não é um número válido!')

# Código alternativo usando isdigit() (mas não aceita números decimais):
# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Erro: Isso não é um número válido!')