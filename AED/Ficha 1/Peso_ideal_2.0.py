
#Peso Ideal 2.0

sexo= input("Indique um sexo (M/F): ")
altura= int(input("Digite a sua altura (cm): "))

if sexo== "M" or "m":
    k=4
    Pesoideal= (altura-100) - (altura-150)/k 
    print("O Peso ideal é {:.1f}".format(Pesoideal))
else:
    k=2
    Pesoideal= (altura-100) - (altura-150)/k 
    print("O Peso real é {:.1f} kg".format(Pesoideal))
