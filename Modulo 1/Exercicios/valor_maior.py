numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))

if numero1 == numero2:
    print("Os numeros são iguais!")
elif numero1 > numero2:
    print(f"{numero1} é maior que {numero2}!")
else:
    print(f"{numero2} é maior que {numero1}!")