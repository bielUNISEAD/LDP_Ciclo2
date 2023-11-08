print ('Esse programa calcula sua idade em anos com base na quantidade dos seus dias de vida ')

i = int(input('Por favor, digite sua idade em dias: '))

# inicia a função
def calcularIdade (i):

    qtdeAnos = i // 365
    qtdeMeses = ((i % 365) // 30)
    qtdeDias = ((i % 365) % 30)


    return qtdeAnos, qtdeMeses, qtdeDias

qtdeAnos, qtdeMeses, qtdeDias = calcularIdade (i)
print(f'Certinho! Sua idade é: {qtdeAnos} anos, {qtdeMeses} meses e {qtdeDias} dias.')