#Capicua

def capicua(word):
    if word==word[::-1]:
        print("A palavra é um capicua")
    else:
        print("A palavra não é uma capicua")

palavra=input("Digite uma palavra:")
capicua(palavra)
