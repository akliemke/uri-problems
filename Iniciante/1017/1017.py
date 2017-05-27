import math

tempo_viagem     = int(raw_input())

velocidade_meida = float(raw_input())


gasto = (tempo_viagem * velocidade_meida) / 12

print("%0.3f" % gasto)
