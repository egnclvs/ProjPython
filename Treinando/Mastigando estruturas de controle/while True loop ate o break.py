﻿#while true - loop até o break
soma = 0
while True:
    x=int(input("Digite o número (0 sai): "))
    if x == 0:
        break
    soma = soma + x
print ("Soma : %s" %soma)
