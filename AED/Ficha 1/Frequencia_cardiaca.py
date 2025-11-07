

#Frequência Cardiaca 2.0

sexo= input("Indique um sexo (M/F): ")
idade = int(input("Digite a sua idade: "))

if sexo== "M":
    FMC= 220-idade
    print("FMC= {:d}".format(FMC))
else:
    FMC= 226-idade
    print("FMC= {:d}".format(FMC))

