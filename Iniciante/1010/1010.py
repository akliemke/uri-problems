
pedido_1 = []
total = 0.0
i = 0

while i < 2:
    pedido_1 = pedido_1 + [raw_input()]
    i += 1


for pedido in range(len(pedido_1)):
    separado = pedido_1[pedido].split(' ', 2)
    total = total + (int(separado[1]) * float(separado[2]))

print("VALOR A PAGAR: R$ %0.2f" % total)
