#Divisão de palavras
"""
def dividir(n1,n2):
    try:
       divisao=n1/n2
       return divisao
    except ZeroDivisionError:
        return "Erro: não é possível dividir por zero."
    
num1= int(input("Digite um número: "))
num2= int(input("Digite outro número: "))
print(dividir(num1,num2))
"""

def dividir():
    try:
       n1=int(input("Digite um número: "))
       n2=int(input("Digite um número: "))
    except ZeroDivisionError:
        return "Erro: não é possível dividir por zero."
    else:
        divisao=n1/n2
        return print(divisao)
    
dividir()