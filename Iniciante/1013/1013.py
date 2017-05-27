valores = raw_input()
maior = 0
separados = valores.split(' ', 3)

a = int(separados[0])
b = int(separados[1])
c = int(separados[0]) - int(separados[1])
c = abs(c)

maiorAB = (a + b + abs(a-b)) / 2

if maiorAB > int(separados[2]):
    maior = maiorAB
else:
    maior = int(separados[2])

print("{0} eh o maior".format(maior))
