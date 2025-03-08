"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# for letter in texto
texto = 'Python'  # iterável

# iteratador = iter(texto)  # iterator

# while True:
#     try:
#         letter = next(iteratador)
#         print(letter)
#     except StopIteration:
#         break

for letter in texto:
    print(letter)