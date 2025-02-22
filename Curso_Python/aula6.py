# Conversão de tipos, coerção
# Type conversion, typecasting, coercion
# É o ato de converter um tipo em outro
# Tipos imutáveis e primitivos:
# str, int, float, bool

# Convertendo string para inteiro
print(int('1'), type(int('1')))  # Saída: 1 <class 'int'>

# Convertendo string para float e somando com um número
print(type(float('1') + 1))  # Saída: <class 'float'> (1.0 + 1 = 2.0)

# Convertendo string vazia para booleano
print(bool(' '))  # True (uma string com espaço não é vazia, então é True)

# Convertendo inteiro para string e concatenando com outra string
print(str(11) + 'b')  # Saída: "11b"



# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
#  tipos imutáveis e primitivos:
# str, int, float, bool
print(int('1'), type(int('1')))
print(type(float('1') + 1))
print(bool(' '))
print(str(11) + 'b')