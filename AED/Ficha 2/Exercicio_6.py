
# Sequencia de Fibonnaci
#repetição

n= int(input(" Digite o número de termos: "))
a=0
b=1

soma=0
print(" Os primeiros {:d} termos da sequência Fibonnaci são:".format(n))
for i in range(n):
    print(a , end=" ")
    soma=a+b
    a=b
    b=soma
    















