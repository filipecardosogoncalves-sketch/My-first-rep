#O índice de massa corporal (IMC) (Categorizar)

Altura = float(input("Digite a sua altura"))
Peso = float(input("Digite o seu peso"))
IMC = Peso/(Altura**2)
print("O seu IMC é: {:.2f}".format(IMC))

if IMC <18.5:
    print("Baixo Peso")
elif 18.5<= IMC <24.9:
    print("Peso Normal")
elif 25<= IMC <29.9:
    print("Excesso de Peso")
elif 30<= IMC <34.9:
    print("Obesidade Grau 1")
elif 35<= IMC <39.9:
    print("Obesidade Grau 2")
else:
    print("Obesidade Mórbida")

# Fim do Codigo