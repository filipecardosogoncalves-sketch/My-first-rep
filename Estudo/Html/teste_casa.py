texto = "Numeros: "

num = 1

while num > 0:
    num = int(input("Numero: "))
    if num > 0:
        texto = texto + str(num) + ", "
    
print(texto)