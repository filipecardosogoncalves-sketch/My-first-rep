

# Segundo maior

n=int(input("Quantos números deseja ler?: "))

maior=0
segundo=0

for i in range(n):
    num=int(input("Digite o {:d} º número: ".format(i+1)))

    if num>maior:
        segundo==maior
        maior==num
    elif num>segundo and num!=maior:
        num==segundo

if maior>segundo:
    print("Segundo maior número:", segundo)
else:
    print(" Não foi possivel determinar o segundo maior número")


    
    






























