
#Fatorial

Num1=int(input("Doigite um Número: "))

fatorial= 1

for i in range(1, Num1+1):
    fatorial*= i

print("O fatorial de {:d} = {:d} ".format(Num1,fatorial))

