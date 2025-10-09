def adicionar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro! Divisão por zero."
    return a / b

print("Selecione a operação:")
print("1. Adição (+)")
print("2. Subtração (-)")
print("3. Multiplicação (*)")
print("4. Divisão (/)")

escolha = input("Digite a opção (1/2/3/4): ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if escolha == '1':
    resultado = adicionar(num1, num2)
elif escolha == '2':
    resultado = subtrair(num1, num2)
elif escolha == '3':
    resultado = multiplicar(num1, num2)
elif escolha == '4':
    resultado = dividir(num1, num2)
else:
    resultado = "Opção inválida"

print(f"O resultado é: {resultado}")