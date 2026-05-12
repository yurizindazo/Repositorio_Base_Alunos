nota = float(input("Digite a sua nota (Notas válidas de 0 até 10): "))

while nota < 0 or nota > 10:
    nota = float(input("Invalido, digite uma nota entre 0 e 10 ")) #o loop so para quando fica incorreto dentro desse cmd

print(f"Sua nota foi: {nota}")