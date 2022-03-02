consumo = int(input('Quantidade em kWh consumida: '))
print('residencias = R')
print('comercios = C')
print('industria = I')
tipo = input('Tipo de instalação: ')
if tipo.upper() == 'R':
    if consumo <= 500:
        pagar = consumo * 0.4
    else:
        pagar = consumo * 0.65
elif tipo.upper() == 'C':
    if consumo <= 1000:
        pagar = consumo * 0.55
    else:
        pagar = consumo * 0.6
elif tipo.upper() == 'I':
    if consumo <= 5000:
        pagar = consumo * 0.55
    else:
        pagar = consumo * 0.6
else:
    print('Tipo inválido')
    pagar = 0
print(f'Total a pagar: R${pagar:.2f}')
