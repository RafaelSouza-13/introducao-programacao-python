horas = input("Digite a quantidade de horas: ")
horas = int(horas)
minutos = input("Digite a quantidade de minutos: ")
minutos = int(minutos)
segundos = input("Digite a quantidade de segundos: ")
segundos = int(segundos)
totalSegundos = horas * 60 * 60 + minutos * 60 + segundos
print(f'Total de segundos = {totalSegundos}')
