"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""

# Exemplo básico de operação ternária
# condicao = 10 == 11  # False, pois 10 não é igual a 11
# variavel = 'Valor' if condicao else 'Outro valor'
# print(variavel)  # Saída: 'Outro valor', pois a condição é False

# Exemplo com números
# digito = 9  # > 9 = 0
# novo_digito = digito if digito <= 9 else 0  # Se digito <= 9, mantém o valor; senão, define como 0
# novo_digito = 0 if digito > 9 else digito  # Outra forma de escrever a mesma lógica
# print(novo_digito)  # Saída: 9, pois digito <= 9

# Exemplo de operação ternária aninhada
print('Valor' if False else 'Outro valor' if False else 'Fim')
# Explicação:
# 1. A primeira condição é False, então avança para o próximo `else`.
# 2. A segunda condição também é False, então avança para o próximo `else`.
# 3. Como todas as condições são False, o valor final é 'Fim'.
# Saída: 'Fim'