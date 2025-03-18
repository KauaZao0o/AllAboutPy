# Desempacotamento em chamadas
# de métodos e funções
string = 'ABCD'
lista = ['Ana', 'Rogério', 1, 2, 3, 'Duda']
tupla = 'Python', 'é', 'legal'
salas = [
    # 0        1
    ['Ana', 'Rogério', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Duda', ],  # 2
]

# p, b, *_, ap, u = lista
# print(p, u, ap)

# print('Ana', 'Rogério', 1, 2, 3, 'Duda')
# print(*lista)
# print(*string)
# print(*tupla)

print(*salas, sep='\n')