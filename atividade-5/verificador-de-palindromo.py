import re # Módulo para expressões regulares, usado para remover caracteres não alfanuméricos

def verificar_palindromo(texto):
    """
    Verifica se uma palavra ou frase é um palíndromo, ignorando espaços e pontuação.

    Parâmetros:
    - texto (str): A palavra ou frase a ser verificada.

    Retorna:
    - str: "Sim" se for um palíndromo, "Não" caso contrário.
    """
    
    # 1. Limpa o texto: remove tudo que não for letra ou número
    texto_limpo = re.sub(r'[^a-zA-Z0-9]', '', texto)
    
    # 2. Converte para minúsculas para garantir a comparação
    texto_formatado = texto_limpo.lower()
    
    # 3. Inverte o texto
    texto_invertido = texto_formatado[::-1]
    
    # 4. Compara o texto original formatado com o invertido
    if texto_formatado == texto_invertido:
        return "Sim"
    else:
        return "Não"

# Exemplos de uso:
frase1 = "Ame o sapo e os sapos ema" # Palíndromo
frase2 = "Python é legal" # Não é palíndromo
frase3 = "Roma me tem amor" # Palíndromo

print(f"'{frase1}' é palíndromo? Resultado: {verificar_palindromo(frase1)}")
print(f"'{frase2}' é palíndromo? Resultado: {verificar_palindromo(frase2)}")
print(f"'{frase3}' é palíndromo? Resultado: {verificar_palindromo(frase3)}")