def calcular_imc():
    """Solicita peso e altura, calcula o IMC e retorna a classificação."""
    try:
        peso = float(input("Digite seu peso em quilogramas (ex: 70.5): "))
        altura = float(input("Digite sua altura em metros (ex: 1.75): "))
    except ValueError:
        print("\nEntrada inválida. Por favor, use números para peso e altura.")
        return

    if peso <= 0 or altura <= 0:
        print("\nPeso e altura devem ser valores positivos.")
        return

    # IMC = peso / (altura * altura)
    imc = peso / (altura ** 2)

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obeso"

    print(f"\nSeu IMC é: {imc:.2f}")
    print(f"Classificação: {classificacao}")

# --- Chamada da função para iniciar o programa ---
calcular_imc()