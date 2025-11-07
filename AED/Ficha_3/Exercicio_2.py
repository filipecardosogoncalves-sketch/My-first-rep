#Número de Caracteres, Vogais e Espaços

def counttext(text): 
   vogais="aeiou"
   espaços=text.count(" ")
   total_vogais=0
   caracteres=len(text)

   for i in vogais:# o for tamb serev
      total_vogais+= text.count(i)


   print(f"Nº de espaços: {espaços}")
   print(f"Nº de vogais: {total_vogais}")
   print(f"Nº de caracteres: {caracteres}")

texto=input("Digite um texto: ")
print(counttext(texto))



