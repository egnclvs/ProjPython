#Acumuladores
n=1
soma=0
while n <= 10:
    x = int(input("Digite o %d número: " %n))
    soma = soma + x
    n = n+1
print("Soma: %d" %soma)
#Imprimindo a média de 10 numeros inteiros
print("Media: %5.2f" %(soma/10))

#calcular o fatorial de 10
n=1
fat=1
while n <= 10:
    x = int(input("Digite o %d número: " %n))
    fat = fat * x
    n = n+1
print("Fatorial: %d " %fat)

#calcular o fatorial de un numero n

c=1
fat=1
n=int(input("Digite um numero: "))
while c <= n:
    fat=fat*c
    c=c+1
print("Fat(%d) = %d" %(n,fat))
