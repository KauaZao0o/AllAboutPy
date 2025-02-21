# Tipos int e float

# int -> Número inteiro
# O tipo int representa qualquer número
# positivo ou negativo. int sem sinal é considerado
# positivo.
print(11)  # int
print(-11)  # int
print(0)  # int (zero é um número inteiro)

# float -> Número com ponto flutuante
# O tipo float representa qualquer número
# positivo ou negativo com ponto flutuante.
# float sem sinal é considerado positivo.
print(1.1)  # float
print(10.11)  # float
print(0.0)  # float (zero também pode ser representado como float)
print(-1.5)  # float (número negativo com ponto flutuante)

# A função type mostra o tipo que o Python
# inferiu ao valor.
print(type('Guido'))  # <class 'str'>: Tipo string
print(type(0))  # <class 'int'>: Tipo inteiro
print(type(1.1), type(-1.1), type(0.0))  # <class 'float'>: Tipos float
