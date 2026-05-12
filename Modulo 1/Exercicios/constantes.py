TAXA_SERVICO = 0.004
PORCENTUAL_IMPOSTO_RENDA_4 = 0.25
PORCENTUAL_IMPOSTO_RENDA_3 = 0.2
PORCENTUAL_IMPOSTO_RENDA_2 = 0.15
PORCENTUAL_IMPOSTO_RENDA_1 = 0.1
FAIXA_SALARIAL_4 = 10000
FAIXA_SALARIAL_3 = 7500
FAIXA_SALARIAL_2 = 5000
FAIXA_SALARIAL_1 = 2500

#Usando as constantes voce guarda uma variavel é pode deixar o comando mais simples e menos poluido
#e podendo alterar a qualquer momentoo

print("Calculadora de imposto")

salario_base = float(input("Digite o quanto voce ganha: "))

if salario_base > FAIXA_SALARIAL_4: 
    imposto = salario_base * (PORCENTUAL_IMPOSTO_RENDA_4 + TAXA_SERVICO)
elif salario_base > FAIXA_SALARIAL_3:
    imposto = (PORCENTUAL_IMPOSTO_RENDA_3 + TAXA_SERVICO)
elif salario_base > FAIXA_SALARIAL_2:
    imposto = salario_base * (PORCENTUAL_IMPOSTO_RENDA_2 + TAXA_SERVICO)
elif salario_base > FAIXA_SALARIAL_1:
    imposto = salario_base * (PORCENTUAL_IMPOSTO_RENDA_1 + TAXA_SERVICO)
else:
    imposto = 0
    taxa_conveniencia = 0

print(f"Para a sua faixa salaria o imposto é: {imposto}")
