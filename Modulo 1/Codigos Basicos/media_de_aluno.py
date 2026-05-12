nome = input("Digite o nome do aluno:")
numero1 = float(input("Digite a nota do aluno:"))
numero2 = float(input("Digite a nota do aluno:"))
numero3 = float(input("Digite a nota do aluno:"))
 
resultado = (numero1 + numero2 + numero3) / 3 
print("A media do aluno é ", resultado )

if resultado >= 7:
    print("O aluno esta aprovado!")
elif resultado > 4:
    print("O aluno esta de recuperação!")
else:
    print("O aluno esta reprovado!")