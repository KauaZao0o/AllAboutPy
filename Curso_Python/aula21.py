# Operadores lógicos: and (E), or (OU) e not (NÃO)

# O operador `and` exige que TODAS as condições sejam verdadeiras.
# Se um dos valores for "falsy" (0, 0.0, '', False, None), a expressão para ali.

entrada = input('[E]ntrar [S]air: ').strip().lower()
senha_digitada = input('Senha: ').strip()

senha_permitida = '123456'

if entrada == 'e' and senha_digitada == senha_permitida:
    print('Acesso permitido!')
else:
    print('Acesso negado!')

# Avaliação de curto-circuito com `and`
print(True and False and True)  # False (para na primeira condição falsa)
print(True and 0 and True)  # 0 (para na primeira condição falsy)

# Teste extra com `or`
print(False or True or False)  # True (para na primeira condição verdadeira)

# Teste extra com `not`
print(not True)  # False
print(not False)  # True