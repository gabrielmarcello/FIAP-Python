# 8 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

qnt_ganha_por_hora = float(input("Digite quanto você ganha por hora: "))
num_horas_trabalhadasMes = float(input("Digite o número do horas trabalhadas no mês: "))

totalSalario = qnt_ganha_por_hora * num_horas_trabalhadasMes

print(f"O total do seu salário no referido mês é de: {totalSalario}")