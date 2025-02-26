nome = 'Fulano Silva'
altura = 1.75
peso = 80
imc = peso / altura ** 2

"f-strings"
linha_1 = f'{nome} tem {altura:.2f}m de altura,'
linha_2 = f'pesa {peso}kg e seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# Fulano Silva tem 1.75m de altura,
# pesa 80kg e seu IMC é
# 26.12