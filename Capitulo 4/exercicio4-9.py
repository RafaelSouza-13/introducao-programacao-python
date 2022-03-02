salario = float(input('Digite seu salário: '))
anos = int(input('Digite a qauntidade de anos a pagar: '))
valor = float(input('Digite o valor da casa: '))
prestacao = valor / (anos * 12)
if prestacao > salario * 30 / 100:
    print('Emprestimo negado!')
else:
    print('Emprestimo aprovado')
print(f'prestação: {prestacao} / 30%: {(salario * 30 / 100)}')
