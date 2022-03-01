salario = input('Digite o salario: ')
salario = float(salario)
percentual = input('digite a porcentagem de aumento: ')
percentual = float(percentual)
ajuste = salario * percentual / 100
salario = salario + ajuste
print(f'Aumento de {percentual}%. Novo salario: {salario:.2f}')
