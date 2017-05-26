numero_funcionario = raw_input()
salario_fixo = float(raw_input())
montante_vendas = float(raw_input())

valor_salario = salario_fixo + (montante_vendas * 0.15)

print("TOTAL = R$ %0.2f" % valor_salario)
