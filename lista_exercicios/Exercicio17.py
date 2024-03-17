#17 - Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
#que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

tamanho_metros_quadrados = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))

litros = tamanho_metros_quadrados / 6

latas18 = math.ceil(litros / 18)
galoes3 = math.ceil(litros / 3.6)

preco_latas18 = latas18 * 80.00
preco_galoes3 = galoes3 * 25.00

latas_para_comprar = math.ceil(litros / 18)
restoLitros = latas_para_comprar * 18 - litros
galoes_para_comprar = math.ceil(restoLitros / 3.6)

preco_misturado = latas_para_comprar * 80 + galoes_para_comprar * 25

print(f"Quantidade de tintas em latas de 18 litros: {latas18}")
print(f"Preço em latas de 18 litros: R${preco_latas18:.2f}")

print(f"Quantidad de tinta em galões de 3.6 litros: {galoes3}")
print(f"Preço em galões de 3.6 litros: R${preco_galoes3:.2f}")

print(f"Para minimizar o desperdício, compre {latas_para_comprar} latas e {galoes_para_comprar} galões.")
print(f"Preço ao misturar: R${preco_misturado:.2f}")