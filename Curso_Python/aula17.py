# if / elif / else
# se / se não se / se não

condicao1 = True
condicao2 = True
condicao3 = True
condicao4 = True

if condicao1:
    print('Código para condição 1')
    print('Código para condição 1')
elif condicao2:
    print('Código para condição 2')  # Este bloco será executado primeiro
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')  # Nunca será executado, pois condicao2 já foi atendida
else:
    print('Nenhuma condição foi satisfeita.')

# Um if separado, não relacionado ao bloco acima
if 10 > 5:
    print('Outro if - Esta condição é verdadeira')

print('Fora do if')  # Sempre será executado