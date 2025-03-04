"""
CONSTANTES -> São variáveis que não devem mudar (por convenção, usamos letras maiúsculas)
Muitas condições no mesmo `if` podem aumentar a complexidade do código, tornando-o difícil de ler e manter.
A contagem de complexidade pode ser reduzida dividindo as verificações em partes menores.
"""

# Definição das variáveis
velocidade = 61  # Velocidade atual do carro
local_carro = 100  # Posição do carro na estrada

# Definição das constantes
RADAR_1 = 60  # Velocidade máxima permitida pelo radar 1
LOCAL_1 = 100  # Localização do radar 1 na estrada
RADAR_RANGE = 1  # Alcance do radar (distância para detectar infração)

# Verifica se o carro está dentro da área de detecção do radar
dentro_do_alcance = LOCAL_1 - RADAR_RANGE <= local_carro <= LOCAL_1 + RADAR_RANGE

# Verifica se o carro ultrapassou a velocidade permitida pelo radar
ultrapassou_velocidade = velocidade > RADAR_1

# Verifica se o carro foi multado
if dentro_do_alcance and ultrapassou_velocidade:
    print('O carro foi multado!')
else:
    print('O carro está dentro do limite de velocidade.')