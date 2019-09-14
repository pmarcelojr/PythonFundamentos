# Calculadora Simples em Python

print("\n*****Calculadora*****")

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x // y

print("Selecione o número da operação desejada!\n")
print("\n 1 - Soma")
print("\n 2 - Subtração")
print("\n 3 - Multiplição")
print("\n 4 - Divisão")

escolha = input("\nQual sua escolha: ")

n1 = int(input("\nDigite o primeiro numero: "))
n2 = int(input("\nDigite o segundo numero: "))

if escolha == '1':
    print("\n")
    print(n1, " + ", n2, " = ", add(n1, n2))
elif escolha == '2':
    print("\n")
    print(n1, " - ", n2, " = ", sub(n1, n2))
elif escolha == '3':
    print("\n")
    print(n1, " * ", n2, " = ", mul(n1, n2))
elif escolha == '4':
    print("\n")
    print(n1, " / ", n2, " = ", div(n1, n2))
else:
    print("Escolha invalida!!")
