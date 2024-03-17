#18 - Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).


tamanho_arquivo = float(input("Digite o tamanho do arquivo: "))
velocidade_link_internet = float(input("Digite a velocidade do link de internet em Mbps: "))

velocidade_link_MBps = velocidade_link_internet / 8

tempo_aproximado_em_segundos = tamanho_arquivo * velocidade_link_MBps

tempo_aproximado_em_minutos = tempo_aproximado_em_segundos / 60

print(f"O tempo aproximado de download do arquivo é de: {tempo_aproximado_em_minutos}")