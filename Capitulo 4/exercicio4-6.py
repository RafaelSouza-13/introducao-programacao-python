distancia = int(input('Digite a distancia que deseja percorrer: '))
if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45
print(f'Distancia de {distancia}km/h, preço a pagar: R${preco:.2f}')
