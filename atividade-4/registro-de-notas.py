notas = []
print("--- Calculadora de Média da Turma ---")
print("Digite 'fim' para parar de inserir notas.")

while True:
    entrada = input("Digite a nota do aluno: ")

    if entrada.lower() == 'fim':
        break
    
    try:
        nota = float(entrada)
        if nota < 0:
            print("Nota inválida. Digite um valor não negativo.")
            continue
        notas.append(nota)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número ou 'fim'.")
        
if notas:
    total_alunos = len(notas)
    soma_notas = sum(notas)
    media_turma = soma_notas / total_alunos
    
    print("-" * 30)
    print(f"Total de alunos registrados: {total_alunos}")
    print(f"Soma total das notas: {soma_notas:.2f}")
    print(f"Média da turma: {media_turma:.2f}")
else:
    print("Nenhuma nota foi registrada.")