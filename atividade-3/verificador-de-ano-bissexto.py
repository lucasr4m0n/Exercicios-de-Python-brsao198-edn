def verificar_ano_bissexto():
    """Verifica se um ano inserido é bissexto."""
    try:
        ano = int(input("Digite o ano para verificar: "))
    except ValueError:
        print("\nEntrada inválida. Digite um número inteiro para o ano.")
        return
    
    if ano < 0:
        print("\nO ano deve ser positivo.")
        return

    # Um ano é bissexto se for:
    # (Divisível por 4 E NÃO divisível por 100) OU (Divisível por 400)
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"\nO ano {ano} é BISSEXTO.")
    else:
        print(f"\nO ano {ano} NÃO é bissexto.")

# --- Chamada da função para iniciar o programa ---
verificar_ano_bissexto()