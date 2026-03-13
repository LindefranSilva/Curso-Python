# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

# print("{} metro(s), convertido(s) em centímetros, é {}cm; convertido(s) em milímetros é {}mm.".format(n, (n*100), (n*1000)))
n = int(input('Digite em metros: \n'))
print('{} metros sao {} kilometros.'.format(n, n * 1000))
print('{} metros sao {} hectometros.'.format(n, n * 100))
print('{} metros sao {} decametros.'.format(n, n * 10))

print('{} metros sao {} metros.'.format(n, n * 1))

print('{} metros sao {} decimetros.'.format(n, n * 10))
print('{} metros sao {} centimetros.'.format(n, n * 100))
print('{} metros sao {} milimetros.'.format(n, n * 1000))