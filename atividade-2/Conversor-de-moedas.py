# 1. Conversor de Moeda

# Dados
valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

# Conversão
dolares = valor_reais / taxa_dolar
euros = valor_reais / taxa_euro

# Exibição dos resultados
print("--- Conversor de Moeda ---")
print(f"Valor em Reais: R$ {valor_reais:.2f}")
print(f"Valor em Dólares: $ {dolares:.2f}")
print(f"Valor em Euros: € {euros:.2f}")
print("-" * 25)