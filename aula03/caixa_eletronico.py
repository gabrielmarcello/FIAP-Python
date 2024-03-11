ced100 = 0
ced50 = 0
ced20 = 0
ced10 = 0
total = 0
resto = 0

while(True):
    saque = int(input("Digite o valor do saque: "))
    total = saque

    if(saque <= 0):
        print("O valor do saque não pode ser negativo! Digite novamente")
    elif(saque % 10 != 0):
        print("O valor do saque não pode ser negativo ou não é múltiplo de 10! Digite novamente")
    else: 
        ced100 = total // 100
        resto = total % 100

        ced50 = resto // 50
        resto = resto % 50

        ced20 = resto // 20
        resto = resto % 20

        ced10 = resto // 10
        resto = resto % 10

        print(f"Será necessário {ced100} nota(s) de R$100")
        print(f"Será necessário {ced50} nota(s) de R$50")
        print(f"Será necessário {ced20} nota(s) de R$20")
        print(f"Será necessário {ced10}  nota(s) de R$10")
        break