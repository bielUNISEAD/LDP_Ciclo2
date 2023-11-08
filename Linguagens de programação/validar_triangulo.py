print ('Esse código verifica se os valores digitados são um triângulo.')

a = int(input('Digite a medida do primeiro lado do triangulo (a): '))
b = int(input('Digite a medida do segundo lado do triangulo (b): '))
c = int(input('Digite a medida do terceiro lado do triangulo (c): '))

# não é triangulo
if a > b + c :
    print(' Não é um triangulo. As medidas não formam um triângulo, pois (a) é maior que (b) + (c).')

#caso contrário, calcula a área. Deve-se encontrar o semiperimetro antes e jogar na Fórmula de Heron. Vale lembrar que o semiperímetro é a metade do perímetro
else:
     p = (a + b + c)/2
     area = ( p * ( p - a ) * ( p - b ) * ( p -c ) ) ** 0.5
# ** 0,5 nesse caso representa a potência de meio, que é a mesma coisa que extrair a raiz.
     print(f' É um triangulo e sua área total é: {area:.2f} ')