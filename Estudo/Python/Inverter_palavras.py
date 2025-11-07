#Inverter palavras

def inverText(text):
    partes=text.split()
    texto_invertido= partes[::-1]
    return " ".join(texto_invertido)

texto=input("Digite um texto: ")
print(inverText(texto))