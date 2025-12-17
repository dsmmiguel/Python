def eh_primo(numero):
    if numero <= 1:
         return False
    for i in range(2, numero):
         if numero % i == 0:
          return False
    return True

numero_escolhido = int(input("Qual o número escolhido?"))

resultado_numero_escolhido = eh_primo(numero_escolhido)
if resultado_numero_escolhido == True:
    print("o numero escolhido é primo")
elif resultado_numero_escolhido == False:
     print("o número escolhido não é primo")
else:
     print("erro")