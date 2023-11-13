# Função para realizar a operação de adição
def adicao(x, y):
    return x + y

# Função para realizar a operação de subtração
def subtracao(x, y):
    return x - y

# Função para realizar a operação de multiplicação
def multiplicacao(x, y):
    return x * y

# Função para realizar a operação de divisão
def divisao(x, y):
    if y == 0:
        return "Erro! Divisão por zero."
    else:
        return x / y

# Função principal que exibe o menu e realiza as operações
def calculadora():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    escolha = input("Digite 1, 2, 3 ou 4 para selecionar a operação: ")

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        print("Resultado: ", adicao(num1, num2))
    elif escolha == '2':
        print("Resultado: ", subtracao(num1, num2))
    elif escolha == '3':
        print("Resultado: ", multiplicacao(num1, num2))
    elif escolha == '4':
        print("Resultado: ", divisao(num1, num2))
    else:
        print("Opção inválida")

# Chama a função da calculadora
calculadora()