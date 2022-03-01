quantidade = input('Quantidade de cigarros fumados ao dia: ')
quantidade = int(quantidade)
anos = input('Quantos anos fumando: ')
anos = int(anos)
diasFumando = anos * 365
tempoDiaperdido = 10 * quantidade
minutosPerdidos = diasFumando * tempoDiaperdido
diasPerdidos = minutosPerdidos / 1440
print(f'Dias perdidos: {diasPerdidos:.0f}')
