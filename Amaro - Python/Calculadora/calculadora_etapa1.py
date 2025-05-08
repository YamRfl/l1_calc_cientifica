# Passo 1: Solicitar ao usuário que insira o números e a operação
numero1 = float(input("Digite o primeiro número: "))
operador = input("Digite o perador (+, -, *, /): ")
numero2 = float(input("Digite o segundo número: "))


#Passo 2: Realiza a operação correspondente
if operador == '+':
    resultado = numero1 + numero2
elif operador == '-':
    resultado = numero1 - numero2
elif operador == '*':
    resultado = numero1 * numero2
elif operador == '/':
    resultado = numero1 / numero2
else:
    resultado = "Operador inválido"

#Passo 3 : Exibir o resultado
print("Resultado:", resultado)