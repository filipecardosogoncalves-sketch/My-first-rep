
#Peso em Diferentes Planetas  # é possivel fazer com case

print("\t\t\t\t Planetas")
print("\t\t\t 1 - Mercúrio")
print("\t\t\t 2 - Vénus")
print("\t\t\t 3 - Marte")
print("\t\t\t 4 - Júpiter")
print("\t\t\t 5 - Saturno")
print("\t\t\t 6 - Urano")
print("\n")

Peso= float(input("Indique o seu peso (Kg): "))
print("\n")
Codigo= int(input("Inque o código de Planeta: "))

if Codigo==1:
     fatorweight= 0.37
     PesoPlanetaX =  Peso* fatorweight / 0.98 
     print("O seu peso {:.2f} Kg no Planeta {:d} seria {:.2f} Kg".format(Peso,Codigo,PesoPlanetaX) )
elif Codigo==2:
     fatorweight= 0.90 
     PesoPlanetaX =  Peso* fatorweight / 0.98 
     print("O seu peso {:.2f} Kg no Planeta {:d} seria {:.2f} Kg".format(Peso,Codigo,PesoPlanetaX) )
elif Codigo==3:
     fatorweight= 0.37 
     PesoPlanetaX =  Peso* fatorweight / 0.98 
     print("O seu peso {:.2f} Kg no Planeta {:d} seria {:.2f} Kg".format(Peso,Codigo,PesoPlanetaX) )
elif Codigo==4:
     fatorweight= 2.53
     PesoPlanetaX =  Peso* fatorweight / 0.98 
     print("O seu peso {:.2f} Kg no Planeta {:d} seria {:.2f} Kg".format(Peso,Codigo,PesoPlanetaX) )
elif Codigo==5:
     fatorweight= 1.06
     PesoPlanetaX =  Peso* fatorweight / 0.98 
     print("O seu peso {:.2f} Kg no Planeta {:d} seria {:.2f} Kg".format(Peso,Codigo,PesoPlanetaX) )
elif Codigo==6:
     fatorweight= 0.91 
     PesoPlanetaX =  Peso* fatorweight / 0.98 
     print("O seu peso {:.2f} Kg no Planeta {:d} seria {:.2f} Kg".format(Peso,Codigo,PesoPlanetaX) )
else:
     print("Número inválido, por favor tente novamente")