"""
Lista de listas e seus índices
"""
salas = [
    # 0        1
    ['Alex', 'Kauã', ],  # Sala 0
    # 0
    ['Rodrigo', ],           # Sala 1
    # 0       1       2
    ['Paulo', 'Pedro', 'Ana', ],  # Sala 2
]

# print(salas[1][0])
# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][3])

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)