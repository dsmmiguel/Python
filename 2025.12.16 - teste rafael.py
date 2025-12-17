def e_primo(num):
    if num <= 1:
        return False
    for divisor in range(2, num):
        if num % divisor == 0:
            return False
    return True


try:
    numero_usuario = int(input("Qual número você escolhe?: "))
    resultado_eh_primo = e_primo(numero_usuario)
    if resultado_eh_primo:
        print(f"O número {numero_usuario} é primo!")
    else:
        print(f"O número {numero_usuario} NÃO é primo!")
except: 
    print("ERRO:")
