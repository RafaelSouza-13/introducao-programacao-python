velocidadeMedia = input('Digite a velocidade media em quilometros por hora: ')
velocidadeMedia = float(velocidadeMedia)
distancia = input('Digite a distancia em quilometros: ')
distancia = float(distancia)
tempo = distancia / velocidadeMedia
print(f'Tempo esperado de {tempo:.2f} horas')
