velocidade = int(input('Qual a velocidade : '))
if velocidade > 110:
    print ("O usuário foi multado pois estava em velocidade de "+str(velocidade)+" Km/h")
    multa = (velocidade-110)*5
    print ("e foi multado em R$ %5.2f" %multa)
