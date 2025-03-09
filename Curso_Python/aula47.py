"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

# Palavra que o usuário deve adivinhar
palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    # Captura uma letra do usuário
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    # Validação para permitir apenas uma letra
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    # Verifica se a letra digitada está na palavra secreta
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    # Monta a palavra com os acertos até o momento
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    # Verifica se o usuário acertou a palavra completa
    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('🎉 VOCÊ GANHOU!! PARABÉNS! 🎉')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0