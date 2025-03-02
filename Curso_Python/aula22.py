# Operadores lógicos: and (E), or (OU) e not (NÃO)

# O operador `or` retorna o primeiro valor verdadeiro encontrado
# Se todos forem "falsy" (0, 0.0, '', False, None), ele retorna o último valor.

entrada = input('[E]ntrar [S]air: ').strip().lower()
senha_digitada = input('Senha: ').strip()

senha_permitida = '123456'

if entrada == 'e' and senha_digitada == senha_permitida:
    print('Acesso permitido!')
else:
    print('Acesso negado!')

# Avaliação de curto-circuito com `or`
senha = input('Digite a senha: ').strip() or 'Sem senha cadastrada'
print(f'Senha definida: {senha}')

# Exemplo extra mostrando como `or` funciona
valor = 0 or False or '' or None or 'Primeiro verdadeiro' or 'Outro valor'
print(f'Valor resultante: {valor}')  # "Primeiro verdadeiro"