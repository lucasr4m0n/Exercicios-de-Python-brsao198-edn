def verificar_senha(senha):
    """Verifica se a senha atende aos critérios de segurança."""
    
    # a - Deve ter pelo menos 8 caracteres
    tamanho_ok = len(senha) >= 8
    
    # b - Deve conter pelo menos um número
    contem_numero = any(char.isdigit() for char in senha)
    
    feedback = []
    valida = True
    
    if not tamanho_ok:
        feedback.append("• Senha deve ter pelo menos 8 caracteres.")
        valida = False
        
    if not contem_numero:
        feedback.append("• Senha deve conter pelo menos um número.")
        valida = False

    return valida, feedback

# Pede a senha ao usuário
senha_usuario = input("Digite a senha para verificação: ")

# Chama a função e exibe o resultado
e_valida, erros = verificar_senha(senha_usuario)

print("-" * 30)
if e_valida:
    print("✅ Senha OK! Atende aos critérios básicos de segurança.")
else:
    print("❌ Senha fraca. Não atende aos critérios:")
    for erro in erros:
        print(erro)