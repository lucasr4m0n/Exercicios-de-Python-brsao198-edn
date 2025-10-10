import random
import string

def gerar_senha_segura():
    """Gera uma senha aleatória com letras, números e símbolos no tamanho desejado pelo usuário."""
    
    # Define os conjuntos de caracteres a serem usados
    letras = string.ascii_letters
    numeros = string.digits
    simbolos = string.punctuation
    
    # Junta todos os caracteres possíveis
    caracteres = letras + numeros + simbolos
    
    while True:
        try:
            # Pede ao usuário o tamanho da senha
            tamanho = int(input("Digite o tamanho desejado para a senha (ex: 12): "))
            if tamanho < 6:
                print("⚠️ O tamanho mínimo recomendado para senhas seguras é 6.")
                continue
            break
        except ValueError:
            print("❌ Entrada inválida. Por favor, digite um número inteiro.")

    # Garante que a senha contenha pelo menos um de cada tipo para ser robusta
    senha = [
        random.choice(letras),
        random.choice(numeros),
        random.choice(simbolos)
    ]
    
    # Preenche o restante da senha com caracteres aleatórios
    for _ in range(tamanho - 3):
        senha.append(random.choice(caracteres))
        
    # Mistura a lista para que a ordem dos caracteres seja aleatória
    random.shuffle(senha)
    
    # Junta os caracteres em uma única string
    senha_final = "".join(senha)
    
    print("-" * 30)
    print(f"🔑 Senha Gerada ({tamanho} caracteres): **{senha_final}**")
    print("-" * 30)

# Chama a função principal
if __name__ == "__main__":
    gerar_senha_segura()