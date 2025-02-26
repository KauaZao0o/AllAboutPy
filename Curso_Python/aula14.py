a = 'XXXXX'
b = 'YYYYYY'
c = 2.5
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)

# Saída:
# b=YYYYYY a=XXXXX a=XXXXX c=2.50