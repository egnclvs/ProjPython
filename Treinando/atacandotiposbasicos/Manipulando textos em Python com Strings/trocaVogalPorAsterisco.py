palavra = "constitucionalicimamente"
cont = 0
qtdLetras = len(palavra)
while cont < qtdLetras:
    if palavra[cont:cont+1] in 'aeiou':
        print(palavra[cont:cont+1])
        palavra[cont:cont+1] = '*' + palavra[cont:cont+1]
    else:
        palavra += palavra[cont:cont+1]
    cont += 1
print(palavra)
print(cont)
# if letras[i] not in 'aeiou':