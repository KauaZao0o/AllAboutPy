# Operador lógico "not"
# Ele inverte o valor booleano da expressão:
# not True -> False
# not False -> True

print(not True)   # False
print(not False)  # True

# Exemplos com valores diferentes de True/False
print(not 0)        # True (0 é considerado falso)
print(not 1)        # False (1 é considerado verdadeiro)
print(not '')       # True (string vazia é falsa)
print(not 'texto')  # False (string não vazia é verdadeira)

# Aplicação prática
senha = input('Digite a senha: ').strip()
if not senha:  # Se a senha estiver vazia
    print('Nenhuma senha foi digitada.')
else:
    print('Senha recebida.')