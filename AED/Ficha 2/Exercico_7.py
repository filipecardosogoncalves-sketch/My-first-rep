#Número perfeito


num = int(input("Digite um número: "))  # Certifica-te que é convertido para inteiro

soma = 0

for i in range(1, num):
    if num % i == 0:
        soma+=i

if soma == num:
    print("O número é perfeito")
else:
    print("O número é imperfeito")

    