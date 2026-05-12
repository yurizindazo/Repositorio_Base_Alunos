nome = input("Qual é o seu nome? ")
idade = input("Qual sua idade? ")

print("-----------------------------")
print("Nome da pessoa:", nome)
print("Idade da pessoa:", idade)
print("-----------------------------")
print(f"Nome da pessoa: {nome}" )
print(f"Idade da pessoa: {idade}")

#f Utilizamos f-strings (strings formatadas). Tudo que estiver entre chaves {} dentro de uma f-string será substituído pelo valor ou expressão correspondente. 
# Essa abordagem permite maior controle e legibilidade, pois podemos inserir variáveis e até mesmo expressões diretamente no texto. 
# resumo:tudo dentro do f-string sera mostrado no texto de comando

Nome_carro = input ("Digite o nome do carro: ")
valor_carro = float(input("Digite o valor do carro: "))
consumo_por_litro = float(input("Digite o consumo por litro: "))
print("-" * 27)
print(f"| Carro: {Nome_carro}")
print(f"| Valor: R$ {valor_carro}")
print(f"| Consumo por litro: {consumo_por_litro}")
print("-" * 27)


