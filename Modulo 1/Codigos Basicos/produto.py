Nome_produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite o porcentual de desconto: "))
valor_desconto = preco * desconto / 100 
preco_final = preco - valor_desconto
print(f"Produto: {Nome_produto} - Preco final: R$ {preco_final}")