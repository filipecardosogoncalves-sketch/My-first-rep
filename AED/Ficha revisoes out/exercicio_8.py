#Codificar Texto

Valores_convertidos=[]

while True:
    entrada= input("Digite um valor: ")

    if entrada.lower()=="sair":
        break

    try:
        numero=int(entrada)
        Valores_convertidos.append(numero)
    except ValueError:
        print("Este valor nao pode ser convertido")

print("\nLista de valores válidos convertidos:")
print(Valores_convertidos)