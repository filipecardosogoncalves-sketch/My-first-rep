
#Codigo binário

num=int(input("Digite um número:" ))
remain=0

if num<1 and num>99:
    print("Número inválido")

numero_binario = ""

while num>1:
    remain = num % 2
    num = num // 2
    numero_binario = str(remain) + numero_binario

numero_binario = "1" + numero_binario

print(numero_binario)
