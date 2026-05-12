peso_usuario = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura:"))

imc = peso_usuario / (altura * altura)
print("O seu imc é de:" , imc)

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 24.4:
    print("Peso normal")
elif imc < 29.9:
    print("Sobrepeso")
elif imc < 34.4:
    print ("Obesidade Grau 1")
elif imc < 39.9:
    print("Obesidade Grau 2")
else:
    print("Obesidade Grau 3")


