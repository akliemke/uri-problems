numero_funcionario = int(raw_input())
horas_trabalhadas = int(raw_input())
salario_hora = float(raw_input())



valor_salario = horas_trabalhadas * salario_hora

print("NUMBER = {0}".format(numero_funcionario))
print("SALARY = U$ %0.2f" % valor_salario)
