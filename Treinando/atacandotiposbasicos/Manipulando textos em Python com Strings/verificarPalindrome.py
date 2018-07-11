while True:
    frase = str(input("Digite uma palavra :"))
    if frase == "saia":
        break
    if frase[::-1] == frase:
        print("A palavra %s é palíndrome" %frase)
    else:
        print("A palavra %s não é palíndrome" %frase)