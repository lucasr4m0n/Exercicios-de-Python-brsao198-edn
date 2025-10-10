import requests

def consultar_cep():
    """Consulta a ViaCEP API e exibe o endereço do CEP digitado pelo usuário."""
    
    cep = input("Digite o CEP para consulta (somente números): ").strip()
    
    # Validação simples do formato do CEP (8 dígitos)
    if not cep.isdigit() or len(cep) != 8:
        print("❌ Erro: Por favor, digite um CEP válido com 8 dígitos.")
        return

    API_URL = f"https://viacep.com.br/ws/{cep}/json/"
    
    try:
        print(f"Buscando informações para o CEP: {cep}...")
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status() 
        
        dados = response.json()
        
        # A ViaCEP retorna uma chave 'erro' se o CEP não existir
        if 'erro' in dados and dados['erro']:
            print("-" * 30)
            print(f"❌ **Falha:** O CEP **{cep}** não foi encontrado.")
            print("-" * 30)
            return

        print("-" * 30)
        print(f"🏡 **Informações do CEP {cep}:**")
        print(f"Logradouro: {dados.get('logradouro', 'N/A')}")
        print(f"Bairro: {dados.get('bairro', 'N/A')}")
        print(f"Cidade: {dados.get('localidade', 'N/A')}")
        print(f"Estado: {dados.get('uf', 'N/A')}")
        print("-" * 30)
        
    except requests.exceptions.RequestException as e:
        print("-" * 30)
        print(f"❌ **Falha na Conexão/Requisição:** Não foi possível acessar a API.")
        print(f"Detalhes do erro: {e}")
        print("-" * 30)
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")

# Chama a função principal
if __name__ == "__main__":
    consultar_cep()