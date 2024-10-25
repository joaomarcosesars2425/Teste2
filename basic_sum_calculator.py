
# Função para soma
def soma(x, y):
    return x + y

# Função principal
def calculadora():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    result = soma(num1, num2)
    print("Resultado da soma: " + str(result))

# Executa a calculadora
calculadora()
