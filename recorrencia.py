# Conversão para radianos
#R = X * 3,1415

# Conversão para radianos
#R = X * 3,1415

X = int(input("Digite um valor entre 0 e 90: "))

while X < 0 or X > 90:
    print("Valor inválido. Precisa estar entre 0 e 90")
    X = int(input("Digite um valor entre 0 e 90: "))


# Não pode usar fatorial nem elevação