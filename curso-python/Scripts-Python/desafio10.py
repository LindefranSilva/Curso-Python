# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# Considere R$ 5.23 = US$ 1 na Data 13/03/26

n = int(input('Quanto dinheiro voce tem? \n R$ '))
dolar = 5.23
conversao = n / dolar
print('Com R$ {} voce pode  comprar US$ {:.2f}'.format(n, conversao))