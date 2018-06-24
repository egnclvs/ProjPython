# -*- coding: utf-8 -*-
qtdMinutos = 0
valorConta = 0
qtdMinutos = int(input('Quantos minutos você falou ? '))
if qtdMinutos < 200:
    valorConta = float(qtdMinutos * 0.20)
else:
    if  qtdMinutos >=200 and qtdMinutos <= 400:
        valorConta = float(qtdMinutos * 0.18)
    else:
        if qtdMinutos > 400 and qtdMinutos <= 800:
            valorConta = float(qtdMinutos * 0.15)
        else:
            valorConta = float(qtdMinutos * 0.08)
print('O Valor da sua conta é R$ %.2f' %valorConta)


qtdMinutos = 0
valorConta = 0
qtdMinutos = int(input('Quantos minutos você falou ? '))
if   qtdMinutos < 200:
    preco=0.20
elif qtdMinutos <=400:
    preco=0.18
elif qtdMinutos <=800:
    preco=0.15
else:
    preco=0.08
print('O Valor da sua conta é R$ %.2f' %(qtdMinutos*preco))
    
