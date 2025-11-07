#Contar palavras

def contar_palavra(text,word):
    list=text.lower().split(" ")
    return print(f"A palvra {word} aparece", list.count(word.lower()))

texto=input("Digite um texto:")
palavra=input("Digite uma palavra para procurar:")
contar_palavra(texto,palavra)