# fatorial de 5: 5 * 4 * 3 * 2 * 1 
def fatorial(n):
    if n <= 1:
        return 1
    else:
        return n * fatorial(n - 1)
# Revisar

# potencia de x^5: x * x * x * x * x 
def potencia(base, expoente):
    if expoente == 0:
        return 1
    elif expoente == 1:
        return base
    else:
        return base * potencia(base, expoente - 1)
# Revisar

def somatoria(x_graus):
    # Converte x de graus para radianos
    r = x_graus * 3.1415 / 180  
    
    # Inicializa a soma
    soma = 0

    # Itera de 0 a 5
    for n in range(6):
        # (-1)^ n
        expressao1 = (-1) ** n
        # Elevação de R
        expressao2 = 2 * n
        # R elevado a expressão 2
        expressao3 = potencia(r, expressao2)
        # Fatorial de (2n)!
        expressao4 = fatorial(expressao2)
        
        # Expressao completa
        expressao = expressao1 * (expressao3 / expressao4)
        
        # Soma o expressao atual à somatória total
        soma += expressao
    
    return soma

# Solicita a entrada do usuário e calcula o cosseno
x = float(input("Digite um valor entre 0 e 90 graus: "))
if 0 <= x <= 90:
    resultado = somatoria(x)
    print(f"O resultado da somatória é: {resultado}")
      # O resultado precisa seguir as regras da saída!
else:
    print("Por favor, insira um valor entre 0 e 90 graus.")
    # Colocar um loop aqui!

# Exemplo de entrada -> 5
# Exemplo de saída -> 0.996

'''
def somatoria (função que é de 0 até 5)

r = x * 3.1415/180
x = input (o <= x <= 90)

exressão1 = (-1) (valor 1 da def somatoria)
exressão1 = (-1)*(-1) (valor 2 da def somatoria)
exressão1 = (-1)*(-1)*(-1) (valor 3 da def somatoria) 
exressão1 = (-1)*(-1)*(-1)*(-1) (valor 4 da def somatoria)
exressão1 = (-1)*(-1)*(-1)*(-1)*(-1) (valor 5 da def somatoria)  

expressao2 = 2  (valor 1 da def somatoria)
expressao2 = 2 * 2 (valor 2 da def somatoria)
expressao2 = 2 * 2 * 2 (valor 3 da def somatoria) 
expressao2 = 2 * 2 * 2 * 2 (valor 4 da def somatoria)
expressao2 = 2 * 2 * 2 * 2 * 2 (valor 5 da def somatoria)  

expressao3 = r ^ expressao2

expressao4 = (2 * (1)) (fatorial do valor 1 da def somatoria)
expressao4 = ( 2 * (2 * 1)) (fatorial do valor 2 da def somatoria)
expressao4 = ( 2 * (3 * 2 * 1)) (fatorial do valor 3 da def somatoria)
expressao4 = ( 2 * (4 * 3 * 2 * 1)) (fatorial do valor 4 da def somatoria)
expressao4 = ( 2 * (5 * 4* 3 * 2 * 1)) (fatorial do valor 5 da def somatoria)

expressao5 = exressão1 * (expressao3/expressao4)

ou seja, vai ficar no final:

(-1)^0 * ( (r)^0 / (0)! ) + (-1)^1 * ( (r)^2 / (2)! ) + (-1)^2 * ( (r)^4 / (4)! ) + (-1)^3 * ( (r)^6 / (6!) ) + (-1)^4 * ( (r)^8 / (8)! ) + (-1)^5 * ( (r)^10 / (10! )
'''