def primo(n):
    if (n <= 1) or (n % 2 == 0 and n > 2):
        return False
    return all(n % i for i in range(3, int(n**0.5) + 1, 2))

# Solicita ao usuário que insira um número
num = int(input('Por favor, digite um número entre 1 e 100: '))

# caso insira fora do intervalo
if num < 1 or num > 100:
    print('Por favor, insira um número entre 1 e 100. ')


else:
# se corresponde a função primo
    if primo(num):
        print(f'{num} é um número primo.')

# se não corresponde a função primo
    else:
        print('Lamento.' f' {num} não é um número primo.')


# loop para testar todos os valores possíveis
print ('')
print ('Testando outros valores...: ')
print ('')

for num in range (1, 101):
    if primo(num):
        print(f"{num} é um primo.")
    else:
        print (f" {num} não é um primo.")