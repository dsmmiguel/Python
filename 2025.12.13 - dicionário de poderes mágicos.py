# dicionário de poderes mágicos
poderes = {
    "leão": "força",
    "águia": "visão aguçada",
    "tartaruga": "defesa"
}

# pergunta o animal
animal = input("Digite um animal: ")

# verifica se o animal existe no dicionário
if animal in poderes:
    print("O", animal, "tem o poder de:", poderes[animal] + "! Incrível!")
else:
    print("Esse animal não está no livro de poderes ")
