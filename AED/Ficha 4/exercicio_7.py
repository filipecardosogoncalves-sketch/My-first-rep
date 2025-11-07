# Encontrar Palavra´

def seachWord(text, word):
    lista = text.lower().split(" ")
    return print(lista.count(word.lower()))


texto=input("Digite um texto: ")
palavra=input("Digite a palavra que quer procurar: ")
seachWord(texto, palavra)