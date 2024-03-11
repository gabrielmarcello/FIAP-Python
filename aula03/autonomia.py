km = 0.0
litro = 0.0
autonomia = 0.0

km = input("Km percorrida: ")
km = float(km)

litro = input("Litros gastos: ")
litro = float(litro)

autonomia = km/litro
print(f"Autonomia: {autonomia:10.2f} km/l")