
def removeSpaces(text):
    text = text.replace("  "," ")# Trocar os dois espaços por um espaço
    return text

text=input("Indique um texto: ")

print("Texto:", removeSpaces(text))