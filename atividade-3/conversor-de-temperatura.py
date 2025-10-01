def converter_temperatura():
    """Converte a temperatura de uma unidade (C/F/K) para outra."""
    print("Unidades disponíveis: C (Celsius), F (Fahrenheit), K (Kelvin)")
    
    try:
        temp = float(input("Digite a temperatura a ser convertida: "))
        origem = input("Unidade de origem (C, F ou K): ").upper()
        destino = input("Unidade de destino (C, F ou K): ").upper()
    except ValueError:
        print("\nEntrada inválida. Digite um número para a temperatura.")
        return

    unidades_validas = ('C', 'F', 'K')
    if origem not in unidades_validas or destino not in unidades_validas:
        print("\nUnidade de origem ou destino inválida. Use C, F ou K.")
        return

    if origem == destino:
        print(f"\nA temperatura já está em {destino}: {temp:.2f}{destino}")
        return

    # 1. Converter para Celsius primeiro
    if origem == 'F':
        temp_celsius = (temp - 32) * 5/9
    elif origem == 'K':
        temp_celsius = temp - 273.15
    else:
        temp_celsius = temp

    # 2. Converter de Celsius para a unidade de destino
    if destino == 'F':
        resultado = (temp_celsius * 9/5) + 32
    elif destino == 'K':
        resultado = temp_celsius + 273.15
    else:
        resultado = temp_celsius

    print(f"\n{temp:.2f}{origem} é igual a {resultado:.2f}{destino}.")

# --- Chamada da função para iniciar o programa ---
converter_temperatura()