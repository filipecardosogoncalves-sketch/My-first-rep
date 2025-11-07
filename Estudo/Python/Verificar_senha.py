# Verificar uma senha

print("\t\t\t\t Digite uma senha que contanha:")
print("\t\t\t\t-Pelo menos uma letra maiúscula")
print("\t\t\t\t -Pelo menos uma letra")
print("\t\t\t\t -Pelo menos um númer")

def verifySenha(senha):
    if len(senha)<8:
        return False

    letras= any(a.isalpha() for a in senha)
    Maiúscula= any(a.isupper() for a in senha)
    digitos= any(a.isdigit() for a in senha)

    return letras and Maiúscula and digitos

code=input("Digite a senha: ")
verifySenha(code)

if verifySenha(code):
    print(" Senha segura!")
else:
    print("Senha Fraca")


