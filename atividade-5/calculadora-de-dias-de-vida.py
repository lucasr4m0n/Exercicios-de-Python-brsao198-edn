from datetime import date

def calcular_dias_de_vida(data_nascimento):
    """
    Calcula o número de dias vividos desde a data de nascimento até a data atual.

    Parâmetros:
    - data_nascimento (date): Objeto date com a data de nascimento.

    Retorna:
    - int: O número total de dias vividos.
    """
    data_atual = date.today()
    
    # A subtração de dois objetos 'date' retorna um objeto 'timedelta'
    diferenca = data_atual - data_nascimento
    
    # O atributo 'days' do timedelta retorna a diferença em dias
    dias_vividos = diferenca.days
    
    return dias_vividos

# Interação com o usuário:
print("--- Calculadora de Dias de Vida ---")

try:
    # Coletando a data de nascimento
    dia = int(input("Digite o dia de nascimento (DD): "))
    mes = int(input("Digite o mês de nascimento (MM): "))
    ano = int(input("Digite o ano de nascimento (AAAA): "))

    # Criando o objeto 'date'
    data_nasc = date(ano, mes, dia)
    
    if data_nasc > date.today():
        print("Erro: A data de nascimento não pode ser no futuro.")
    else:
        dias_vivos = calcular_dias_de_vida(data_nasc)

        print("\n--- Resultado ---")
        print(f"Data de nascimento: {data_nasc.strftime('%d/%m/%Y')}")
        print(f"Você está vivo há **{dias_vivos}** dias!")

except ValueError:
    print("Erro: A data inserida é inválida. Certifique-se de usar números inteiros (AAAA, MM, DD) e que a data exista.")