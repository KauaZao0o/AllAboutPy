# if / elif / else
# se / se não se / se não
entrada = input('Você quer "entrar" ou "sair"? ').strip().lower()  # Remove espaços extras e converte para minúsculas

if entrada == 'entrar':
    print('Você entrou no sistema!')
    print(12341234)
elif entrada == 'sair':
    print('Você saiu do sistema.')
else:
    print('Opção inválida! Digite "entrar" ou "sair".')

print('FORA DOS BLOCOS')