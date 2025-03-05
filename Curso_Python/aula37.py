"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
contador = 0

while contador <= 100:
    contador += 1  # Incremento do contador

    # Se o número for 6, pula para a próxima iteração
    if contador == 6:
        print('Não vou mostrar o 6.')
        continue

    # Se o número estiver entre 10 e 27, pula a iteração
    if 10 <= contador <= 27:
        print('Não vou mostrar o', contador)
        continue

    # Exibe o número normalmente
    print(contador)

    # Para o loop quando chegar a 40
    if contador == 40:
        break

print('Acabou')