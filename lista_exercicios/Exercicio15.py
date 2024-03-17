# 15 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:

qnt_ganha_por_hora = float(input("Digite quanto você ganha por hora: "))
qnt_horas_trabalhadas_mes = float(input("Digite a quantidade de horas trabalhadas no mês: "))

salario_bruto = qnt_ganha_por_hora * qnt_horas_trabalhadas_mes
imposto_renda = 0.11 * salario_bruto
inss =  0.08 * salario_bruto
sindicato = 0.05 * salario_bruto
descontos = imposto_renda + inss + sindicato
salario_liquido = salario_bruto - descontos 

print(f"Salário Bruto: R${salario_bruto:.2f}")
print(f"Imposto de Renda (11%) R${imposto_renda:.2f}")
print(f"INSS R${inss:.2f}")
print(f"Sindicato: R${sindicato:.2f}")
print(f"Salário Liquido: R${salario_liquido:.2f}")