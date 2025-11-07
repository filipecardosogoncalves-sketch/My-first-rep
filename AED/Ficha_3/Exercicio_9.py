#Printar número de caractreser por linha

def printCharLine(texto,numberChar):
    while (len(texto)>numberChar):
        print(texto[0:numberChar])
        texto=texto[numberChar:]
    print(texto)

texto = input("Digite um texto: ")
numberChar = int(input("Números de caracteres por linha: "))
printCharLine(texto,numberChar)