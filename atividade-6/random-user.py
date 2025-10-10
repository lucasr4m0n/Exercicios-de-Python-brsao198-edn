import requests

def buscar_usuario_ficticio():
    """Acessa a RandomUser API para buscar e exibir dados de um usuário aleatório."""
    
    API_URL = "https://randomuser.me/api/"
    
    try:
        # Faz a requisição à API
        print("Buscando usuário aleatório...")
        response = requests.get(API_URL, timeout=10)
        
        # Verifica se a resposta HTTP foi bem-sucedida (código 200)
        response.raise_for_status() 
        
        dados = response.json()
        
        # Extrai as informações do primeiro usuário retornado
        usuario = dados['results'][0]
        
        nome_completo = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']
        
        print("-" * 30)
        print("👤 **Dados do Usuário Fictício:**")
        print(f"Nome: {nome_completo}")
        print(f"E-mail: {email}")
        print(f"País: {pais}")
        print("-" * 30)
        
    except requests.exceptions.RequestException as e:
        # Captura erros de conexão, timeout ou status HTTP
        print("-" * 30)
        print(f"❌ **Falha na Conexão/Requisição:** Não foi possível acessar a API.")
        print(f"Detalhes do erro: {e}")
        print("-" * 30)
    except (KeyError, IndexError):
        # Captura erros se a estrutura JSON da resposta for inesperada
        print("-" * 30)
        print("❌ **Falha:** A API retornou dados em um formato inesperado.")
        print("-" * 30)

# Chama a função principal
if __name__ == "__main__":
    buscar_usuario_ficticio()