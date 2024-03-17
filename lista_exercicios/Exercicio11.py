# 11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

produto = (num1 * 2) * (num2 / 2)
soma = (num1 * 3) + num3
elevado = num3 ** 3

print(f"o produto do dobro do primeiro com metade do segundo é : {produto}")
print(f"a soma do triplo do primeiro com o terceiro é: {soma}")
print(f"o terceiro elevado ao cubo é: {elevado}")