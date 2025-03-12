"""
Exercício
Exiba os índices da lista
0 Ana
1 Sofia
2 Pedro
"""
lista = ['Ana', 'Sofia', 'Pedro']
lista.append('Douglas')


indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))