"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""
string = '1000'
# outra_variavel = f'{string[:3]}ABC{string[4:]}'
# print(string)
# print(outra_variavel)
# Preenchendo com zeros à esquerda até que tenha 10 caracteres
print(string.zfill(10))  # Saída: 0000001000