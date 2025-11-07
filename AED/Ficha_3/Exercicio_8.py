#Texto invertido

def reverseWords(text):
    palavras = text.split()
    texto_invertido = palavras[::-1]
    return " ".join(texto_invertido)


texto=input("Escreve um texto: ")
print(reverseWords(texto))