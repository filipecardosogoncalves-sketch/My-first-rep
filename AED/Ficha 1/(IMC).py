#O índice de massa corporal (IMC)

Altura = float(input("Digite a sua altura"))
Peso = float(input("Digite o seu peso"))
IMC = Peso/(Altura**2)

print("Altura (m):", Altura)
print("Peso (kg):", Peso)
print("O seu IMC é: {:.2f}".format(IMC))