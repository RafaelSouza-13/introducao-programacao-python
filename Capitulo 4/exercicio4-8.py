n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
print('multiplicação = *')
print('divisão = /')
print('soma = +')
print('subtração = -')
operacao = input('Digite a operacao que deseja fazer: ')
if operacao == '+':
    resultado = n1 + n2
elif operacao == '-':
    resultado = n1 - n2
elif operacao == '*':
    resultado = n1 * n2
elif operacao == '/':
    resultado = n1 / n2
else:
    print('Operação inválida!')
    resultado = 'Inválido'
print(f'O resultado da operação é: {resultado}')
