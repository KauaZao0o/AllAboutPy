# Loop principal que percorre valores de 0 a 9
for i in range(10):
    # Se i for igual a 2, exibe a mensagem e pula para a próxima iteração
    if i == 2:
        print('i é 2, pulando...')
        continue  # O continue faz com que o restante do código dentro do loop seja ignorado e vá para a próxima iteração

    # Se i for igual a 8, exibe a mensagem e interrompe o loop principal
    if i == 8:
        print('i é 8, seu else não executará')
        break  # O break encerra o loop imediatamente

    # Loop aninhado que percorre os valores de j entre 1 e 2
    for j in range(1, 3):
        print(i, j)  # Exibe os valores de i e j

# O bloco else do for só será executado se o loop principal terminar normalmente, sem interrupção pelo break
else:
    print('For completo com sucesso!')  # Como há um break em i == 8, esse else nunca será executado