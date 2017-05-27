
valor_inicial = int(raw_input())


cedulas_100 = int(valor_inicial / 100)
valor = (valor_inicial - (cedulas_100 * 100))


cedulas_50 = int(valor / 50)
valor = (valor - (cedulas_50 * 50))

cedulas_20 = int(valor / 20)
valor = (valor - (cedulas_20 * 20))

cedulas_10 = int(valor / 10)
valor = (valor - (cedulas_10 * 10))

cedulas_5 = int(valor / 5)
valor = (valor - (cedulas_5 * 5))

cedulas_2 = int(valor / 2)
valor = (valor - (cedulas_2 * 2))

cedulas_1 = int(valor / 1)
valor = (valor - (cedulas_1 * 1))


print (valor_inicial)
print("{0} nota(s) de R$ 100,00".format(cedulas_100))
print("{0} nota(s) de R$ 50,00".format(cedulas_50))
print("{0} nota(s) de R$ 20,00".format(cedulas_20))
print("{0} nota(s) de R$ 10,00".format(cedulas_10))
print("{0} nota(s) de R$ 5,00".format(cedulas_5))
print("{0} nota(s) de R$ 2,00".format(cedulas_2))
print("{0} nota(s) de R$ 1,00".format(cedulas_1))
