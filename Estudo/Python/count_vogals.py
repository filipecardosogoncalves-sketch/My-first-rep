#Contar vogais

def countVogals(text):
    vogais="aeiou"
    total_vogais=0
    for letra in text:
        if letra in vogais:
            total_vogais += 1

    return print(f"A palavra tem {total_vogais} vogais")

texto=input("Digite um texto: ")
countVogals(texto)
    
    