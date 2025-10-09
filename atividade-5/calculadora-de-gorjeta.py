def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    """
    Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.

    Parâmetros:
    - valor_conta (float): O valor total da conta.
    - porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%).

    Retorna:
    - float: O valor da gorjeta calculada.
    """
    # Converte a porcentagem de um valor inteiro (ex: 10) para decimal (0.10)
    taxa_decimal = porcentagem_gorjeta / 100
    
    # Calcula o valor da gorjeta
    valor_gorjeta = valor_conta * taxa_decimal
    
    # Arredonda o valor para duas casas decimais (centavos)
    return round(valor_gorjeta, 2)

# Exemplo de uso:
conta_total = 75.50
gorjeta_percentual = 15  # 15%

gorjeta = calcular_gorjeta(conta_total, gorjeta_percentual)

print(f"Valor da conta: R$ {conta_total:.2f}")
print(f"Porcentagem de gorjeta: {gorjeta_percentual}%")
print(f"O valor da gorjeta a ser deixada é: R$ {gorjeta:.2f}")