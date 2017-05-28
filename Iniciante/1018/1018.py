
valor_inicial = int(raw_input())
valor = valor_inicial
cedulas = []
notas = [100, 50, 20, 10, 5, 2, 1]

for nota in range(len(notas)):
    cedulas.append(int(valor / notas[nota]))
    valor = (valor - (cedulas[nota] * notas[nota]))

print (valor_inicial)

for n in range(len(cedulas)):
    print("{0} nota(s) de R$ {1},00".format(cedulas[n], notas[n]))
