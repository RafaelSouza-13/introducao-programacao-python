salario = float(input('Digite seu salário: '))
base = salario
if base > 1250:
    salario = salario + ((salario * 10) / 100)
    base = 1251
if base <= 1250:
    salario = salario + ((salario * 15) / 100)
print(f'Novo salario: R${salario:.2f}')
