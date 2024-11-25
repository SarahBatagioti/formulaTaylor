def potencia_recursiva(base, expoente):
    # Potência recursiva (base^expoente)
    if expoente == 0:
        return 1
    return base * potencia_recursiva(base, expoente - 1)

def fatorial_recursivo(n):
    # Fatorial recursivo
    if n <= 1:
        return 1
    return n * fatorial_recursivo(n - 1)

def termo_cosseno(r, n):
    # Cálculo do n-ésimo termo da série
    expressao1 = -1 if n % 2 == 1 else 1  # (-1)^n
    expressao2 = 2 * n  # Potência do numerador
    expressao3 = potencia_recursiva(r, expressao2)  # Numerador calculado recursivamente
    expressao4 = fatorial_recursivo(expressao2)  # Fatorial do denominador
    return expressao1 * (expressao3 / expressao4)

def somatoria_recursiva(r, n):
    # Base da recursão: quando n atinge 0, retorna o termo inicial
    if n == 0:
        return termo_cosseno(r, 0)
    # Recursão: soma o termo atual ao restante da série
    return termo_cosseno(r, n) + somatoria_recursiva(r, n - 1)

def arredondar_para_3_casas(valor):
    # Converte o número para string com precisão maior para avaliar a quarta casa
    valor_str = f"{valor:.4f}"  # Quatro casas decimais
    parte_inteira, parte_decimal = valor_str.split(".")
    
    # Verifica a quarta casa
    if int(parte_decimal[3]) >= 7:
        # Se a quarta casa for >= 7, arredonda a terceira casa para cima
        return round(valor, 3)
    else:
        # Caso contrário, mantém o valor truncado em 3 casas
        return float(f"{parte_inteira}.{parte_decimal[:3]}")

def calcula_cosseno(x_graus):
    # Converte graus para radianos
    r = x_graus * 3.1415 / 180
    # Calcula a série de Taylor para o cosseno até n = 5
    soma = somatoria_recursiva(r, 5)
    # Aplica o arredondamento específico
    return arredondar_para_3_casas(soma)

# Loop para garantir entrada válida
while True:
    try:
        x = float(input("Digite um valor entre 0 e 90 graus: "))
        if 0 <= x <= 90:
            resultado = calcula_cosseno(x)
            print(f"O cosseno de {x:.1f} graus é: {resultado:.3f}")
            break
        else:
            print("Por favor, insira um valor válido entre 0 e 90 graus.")
    except ValueError:
        print("Entrada inválida. Tente novamente.")
