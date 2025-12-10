print("=== MERCADINHO DA PROGRAMAÇÃO ===\n")

preco_pera = 3.50
preco_abobora = 4.50
preco_melancia = 6.99

qtd_pera = int(input(f"Peras (R$ {preco_pera} cada): "))
qtd_abobora = int(input(f"Abóboras (R$ {preco_abobora} cada): "))
qtd_melancia = int(input(f"Melancias (R$ {preco_melancia} cada): "))

total = qtd_pera * preco_pera + qtd_abobora * preco_abobora + qtd_melancia * preco_melancia

print("\n=== NOTINHA ===")
if qtd_pera > 0:
    print(f"{qtd_pera} peras    → R$ {qtd_pera * preco_pera:.2f}")
if qtd_abobora > 0:
    print(f"{qtd_abobora} abóboras → R$ {qtd_abobora * preco_abobora:.2f}")
if qtd_melancia > 0:
    print(f"{qtd_melancia} melancias → R$ {qtd_melancia * preco_melancia:.2f}")

print("─" * 25)
print(f"TOTAL DA COMPRA: R$ {total:.2f}")
print("Volte sempre! 😄")