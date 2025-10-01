def classificar_idade():
    """Solicita a idade e retorna a categoria."""
    try:
        idade = int(input("Por favor, digite sua idade: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
        return # Sai da função se a entrada for inválida

    if idade < 0:
        categoria = "Idade inválida (não pode ser negativa)."
    elif idade <= 12:
        categoria = "Criança"
    elif idade <= 17:
        categoria = "Adolescente"
    elif idade <= 59:
        categoria = "Adulto"
    else: # idade >= 60
        categoria = "Idoso"

    print(f"\nSua idade é {idade} anos.")
    print(f"Classificação: {categoria}.")

# --- Chamada da função para iniciar o programa ---
classificar_idade()