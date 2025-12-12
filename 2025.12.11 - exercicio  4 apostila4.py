# Verificador de Carteira de Motorista

print("VERIFICADOR DE CARTEIRA DE MOTORISTA")
print("=" * 40)

idade = int(input("Quantos anos você tem? "))

if idade == 18:
    print("Hoje é seu dia de fazer a carteira!")
    print("Você pode dirigir!")
elif idade > 18:
    print("Você pode dirigir!")
else:
    print("Ainda não pode dirigir, espere mais um pouco!")