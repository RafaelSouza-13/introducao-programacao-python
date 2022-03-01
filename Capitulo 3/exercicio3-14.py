kmPercorridos = input('Quantidade de km percorridos: ')
kmPercorridos = float(kmPercorridos)
diasAlugado = input('Quantidade de dias alugado: ')
diasAlugado = int(diasAlugado)
valor = diasAlugado * 60 + kmPercorridos * 0.15
print(f'Valor a pagar: R${valor:.2f}')
