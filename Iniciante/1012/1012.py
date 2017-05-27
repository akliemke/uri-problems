
pi = 3.14159
valores = raw_input()

separados = valores.split(' ', 3)

area_triangulo = (float(separados[0]) * float(separados[2]))/2
raio_circulo = area = pi * float(separados[2]) ** 2
area_trapezio = ((float(separados[0]) + float(separados[1])) * float(separados[2])) / 2
area_quadrado = float(separados[1]) ** 2
area_retangulo = float(separados[0]) * float(separados[1])

print("TRIANGULO: %0.3f" % area_triangulo)
print("CIRCULO: %0.3f" % raio_circulo)
print("TRAPEZIO: %0.3f" % area_trapezio)
print("QUADRADO: %0.3f" % area_quadrado)
print("RETANGULO: %0.3f" % area_retangulo)
