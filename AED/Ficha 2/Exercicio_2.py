 # Soma dos numeros compreendidos entre um intervalo de dois números

nummenor=int(input("Número menor: "))
nummaior=int(input("Número maior: "))

soma=0
for i in range(nummenor,nummaior+1):
    if i % 2==0:
        soma+= i 

print("A soma de todos os números compreendidos dentro do intervalo de {:d} e {:d} é {:d}".format(nummenor, nummaior, soma))


