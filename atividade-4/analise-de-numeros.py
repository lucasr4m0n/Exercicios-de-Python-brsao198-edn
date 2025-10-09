pares = 0
impares = 0
print("--- Analisador de Números ---")
print("Digite 'sair' para encerrar a inserção de números.")

while True:
    entrada = input("Digite um número inteiro: ")
    
    if entrada.lower() == 'sair':
        break
    
    try:
        numero = int(entrada)
        
        # Verifica se o número é par (resto da divisão por 2 é 0) ou ímpar
        if numero % 2 == 0:
            pares += 1
            print(f"[{numero}] é PAR.")
        else:
            impares += 1
            print(f"[{numero}] é ÍMPAR.")
            
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro ou 'sair'.")

print("-" * 30)
print("Análise Finalizada!")
print(f"Total de números PARES inseridos: {pares}")
print(f"Total de números ÍMPARES inseridos: {impares}")