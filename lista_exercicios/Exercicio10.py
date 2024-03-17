# 10 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit. (0 °C × 9/5) + 32 = 32 °F


temperatura_celsius = float(input("Digite a temperatura em graus Celsius: "))

temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32

print(f"Temperatura em Fahrenheit é igual a: {temperatura_fahrenheit:.2f}°")
