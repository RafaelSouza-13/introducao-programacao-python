velocidade = int(input('Digite a velocidade do carro: '))
if velocidade > 80:
    multa = (velocidade - 80) * 5
    print(
        f'Velocidade de {velocidade}km/h a cima da média 80km/h, valor da multa por km a cima R${multa:.2f}')
