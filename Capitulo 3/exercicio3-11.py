preco = input('Digite o preço da mercadoria: ')
preco = float(preco)
percentual = input('Digite o percentual de desconto: ')
percentual = float(percentual)
desconto = (preco * percentual) / 100
novoPreco = preco - desconto
print(f'Valor do desconto R${desconto:.2f}, preço a pagar R${novoPreco:.2f}')
