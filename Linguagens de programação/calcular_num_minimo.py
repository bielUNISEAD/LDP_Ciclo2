print ('Esse programa calcula o mínimo entre 3 números digitados e imprime')

num1 = int(input('Por favor, insira o primeiro número: '))
num2 = int(input('Agora insira o segundo número: '))
num3 = int(input('Agora insira o terceiro número: '))

minimo = num1

# se o numero 2 for menor
if (num2<num1 and num2<num3):
   minimo = num2

# se o numero 3 for menor
if (num3<num2 and num3<num1):
   minimo = num3

print(' Número mínimo: {}'.format(minimo))