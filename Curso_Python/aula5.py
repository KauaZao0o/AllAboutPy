# Tipo de dado bool (boolean)
# Ao questionar algo em um programa,
# só existem duas respostas possíveis:
# sim (True) ou não (False).

# O operador == (igualdade) verifica se dois valores são iguais.
print(10 == 10)  # Sim => True (Verdadeiro)
print(10 == 11)  # Não => False (Falso)

# A função type() mostra o tipo do dado
print(type(True))  # <class 'bool'>
print(type(False))  # <class 'bool'>
print(type(10 == 10))  # <class 'bool'> (resultado de uma comparação)
print(type(10 == 11))  # <class 'bool'> (resultado de uma comparação)

# Usando operadores lógicos com bool
print(5 > 3)   # True (5 é maior que 3)
print(5 < 3)   # False (5 não é menor que 3)
print(7 >= 7)  # True (7 é maior ou igual a 7)
print(8 <= 4)  # False (8 não é menor ou igual a 4)
print(9 != 2)  # True (9 é diferente de 2)
print(9 != 9)  # False (9 não é diferente de 9)

# Booleanos em condições
idade = 18
maior_de_idade = idade >= 18
print(maior_de_idade)  # True, pois 18 é maior ou igual a 18

senha_correta = "1234"
print(senha_correta == "1234")  # True
print(senha_correta == "4321")  # False