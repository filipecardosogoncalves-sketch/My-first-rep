
# Números Primos


num= int(input("Digite um número: "))

if num<1 and num>1000:
     print("Número inválido")
elif num==1:
     print("O número 1 não é primo")
else:
     for i in range(2,num):
          if num%i==0:
               print("O número {:d} não é primo".format(num))
               break
          else:
               print("O número {:d} é primo".format(num))
               break


    
    

    