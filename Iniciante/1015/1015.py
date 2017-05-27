import math

p1 = raw_input()
p2 = raw_input()

p1 = p1.split(' ', 2)
p2 = p2.split(' ', 2)


bloco1 = float((float(p2[0]) - float(p1[0])) ** 2)
bloco2 = float((float(p2[1]) - float(p1[1])) ** 2)
distancia_pontos = float(bloco1 + bloco2)
distancia_pontos = math.sqrt(distancia_pontos)
print("%0.4f" % distancia_pontos)
