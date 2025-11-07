#Capicua
def capicua(text):# Introduzir a função capicua
    if text==text[::-1]:
      return True

text=input("Indique um texto: ")
    
if capicua(text):# Verificar a veracidade da função
    print(f"\n\n\n A palavra {text} é uma capicua")
else:
    print(f"\n\n\n A palavra {text} não é uma capicua")
      

