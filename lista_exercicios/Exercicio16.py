# 16 - Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
#Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

import math

tamanho_metros_quadrados = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))

litros = tamanho_metros_quadrados / 3

latas = 18 / litros
latas = math.ceil(latas)

precoTotal = latas * 80.00

print(f"A quantidade de latas a serem compradas é de: {latas}")
print(f"O preço total é de: R${precoTotal:.2f}")

