# Parênteses () → Definem a ordem de execução primeiro.
# Exponenciação ** → Potenciação tem a segunda maior prioridade.
# Multiplicação *, Divisão /, Divisão inteira //, Módulo % → São avaliados da esquerda para a direita.
# Adição + e Subtração - → Executadas por último, seguindo a ordem da esquerda para a direita.
result = (2 + int(1.4 + 0.6)) ** (3 + 3)
print(result)