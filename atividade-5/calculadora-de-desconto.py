def calcular_desconto_e_preco_final(preco_original, porcentagem_desconto):
    """
    Calcula o valor do desconto e o preço final de um produto.

    Parâmetros:
    - preco_original (float): O preço do produto antes do desconto.
    - porcentagem_desconto (float): A porcentagem de desconto (ex: 20 para 20%).

    Retorna:
    - tuple: (valor_desconto, preco_final) arredondados para 2 casas decimais.
    """
    # Converte a porcentagem para um valor decimal
    taxa_desconto = porcentagem_desconto / 100
    
    # a - Cálculo de desconto
    valor_desconto = preco_original * taxa_desconto
    
    # b - Preço final
    preco_final = preco_original - valor_desconto
    
    # c - Formatação: Arredonda o resultado para 2 casas decimais
    return round(valor_desconto, 2), round(preco_final, 2)

# Interação com o usuário:
try:
    preco = float(input("Digite o preço original do produto: R$ "))
    desconto_perc = float(input("Digite a porcentagem de desconto (ex: 15): "))

    if preco < 0 or desconto_perc < 0:
        print("Erro: O preço e a porcentagem de desconto devem ser valores não negativos.")
    elif desconto_perc > 100:
        print("Erro: O desconto não pode ser maior que 100%.")
    else:
        valor_desconto, preco_final = calcular_desconto_e_preco_final(preco, desconto_perc)
        
        # Exibição formatada
        print("\n--- Resultado do Desconto ---")
        print(f"Preço Original: R$ {preco:.2f}")
        print(f"Desconto Aplicado: {desconto_perc:.1f}%")
        print(f"Valor do Desconto: R$ {valor_desconto:.2f}")
        print(f"Preço Final a Pagar: R$ {preco_final:.2f}")
        
except ValueError:
    print("Erro: Por favor, digite valores numéricos válidos.")