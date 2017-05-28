valores = raw_input()
menu = [4.0, 4.5, 5.0, 2.0, 1.50]
separados = valores.split(' ', 2)

total = int(separados[1]) * float(menu[(int(separados[0])-1)])

print("Total: R$ {:0.2f}".format(total))
