#VALIDAÇÂO


List=[]

while True:
    try:
      text = input("Digite uma palavra: ")
      List.append(text)
    except ValueError:
       print("Valor inválido")
       continue

    if text=="Sair" or text=="sair":
       break
