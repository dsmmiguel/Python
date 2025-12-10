preco_pera = 3.5
preco_abobora = 4.5
preco_melancia = 6.99

#Entrada de dados
quantidade_pera = int(input("informe a quantidade de peras que deseja comprar: "))         
quantidade_abobora = int(input("informe a quantidade de aboboras que deseja comprar: "))
quantidade_melancia = int(input("informe a quantidade de melancias que deseja comprar: "))

#Calculo
valor_total = (quantidade_pera * preco_pera) + (quantidade_abobora * preco_abobora) + (quantidade_melancia * preco_melancia)

# Exibir
print(f"O valor total da compra:R$ {valor_total: .2f}")