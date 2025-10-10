import requests
import datetime

def consultar_cotacao_final():
    """Consulta a cotação de uma moeda em relação ao BRL usando Awesomeapi."""
    
    moeda_sigla = input("Digite a sigla da moeda para consulta (ex: USD, EUR): ").upper().strip()
    
    # Monta o par de moedas COM HÍFEN para a URL da API (ex: USD-BRL)
    PAR_URL = f"{moeda_sigla}-BRL"
    API_URL = f"https://economia.awesomeapi.com.br/json/last/{PAR_URL}"
    
    # Monta o nome da chave que virá no JSON de retorno (ex: USDBRL)
    PAR_CHAVE = f"{moeda_sigla}BRL"
    
    try:
        print(f"Buscando cotação para {moeda_sigla} em relação ao Real (BRL)...")
        response = requests.get(API_URL, timeout=10)
        
        # Se a moeda não existir, a API pode retornar 404, que será capturado aqui.
        response.raise_for_status()
        
        dados = response.json()
        
        # Verifica se o par de moedas esperado está na resposta (USDBRL)
        if not dados or PAR_CHAVE not in dados:
            # Esta verificação agora é mais robusta, mas o 404 já deve ter pego o erro.
            print("-" * 30)
            print(f"❌ **Erro:** A moeda **{moeda_sigla}** não foi encontrada.")
            print("-" * 30)
            return
        
        cotacao = dados[PAR_CHAVE]
        
        # Formata a data de atualização
        timestamp = int(cotacao.get('timestamp'))
        data_atualizacao = datetime.datetime.fromtimestamp(timestamp).strftime('%d/%m/%Y %H:%M:%S')

        print("-" * 30)
        print(f"📈 **Cotação {moeda_sigla}/BRL:**")
        # Usamos .get() com um valor padrão para evitar erros caso alguma chave esteja faltando
        print(f"Valor Atual (Compra): R$ {float(cotacao.get('bid', 0)):.4f}")
        print(f"Valor Máximo (High): R$ {float(cotacao.get('high', 0)):.4f}")
        print(f"Valor Mínimo (Low): R$ {float(cotacao.get('low', 0)):.4f}")
        print(f"Última Atualização: {data_atualizacao}")
        print("-" * 30)
        
    except requests.exceptions.RequestException as e:
        # Mensagem de falha genérica para erros de conexão, timeout ou 404
        print("-" * 30)
        print(f"❌ **Falha na Conexão/Requisição:** Não foi possível acessar a API.")
        print(f"Detalhes do erro: {e}")
        print("-" * 30)
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")

# Chame a nova função principal
if __name__ == "__main__":
    consultar_cotacao_final()