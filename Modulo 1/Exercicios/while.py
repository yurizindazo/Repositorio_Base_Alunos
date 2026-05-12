numero = int(input("Digite um numero: "))
numero_começo = int(input("Digite onde deseja começar a tabuada:"))
numero_final = int(input("Digite ate onde o multiplicador deva ir:"))

# for i in range(numero_começo, numero_final + 1):
#     print(f"{numero} x {i} = {numero * 1} 


while numero_começo <= numero_final:
    print(f"{numero} x {numero_começo} = {numero * numero_começo} ")
    numero_começo += 1
