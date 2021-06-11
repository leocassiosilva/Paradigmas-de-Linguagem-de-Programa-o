def exibirMenu():
    print("****MENU****\n")
    print("0 - SAIR\n")
    print("1 - SOMAR\n")
    print("2 - SUBTRAIR\n")
    print("3 - MULTIPLICAR\n")
    print("4 - DIVIDIR\n")
    opcao = int(input("Entre com um numero: "))
    return opcao

def somar(num1, num2):
    resultado = num1+num2
    return resultado

def sub(num1, num2):
    resultado = num1 - num2
    return resultado

def mult(num1, num2):
    resultado = num1 * num2
    return resultado

def div(num1, num2):
    resultado = num1 / num2
    return resultado
    

i=0
opcao=1
num1 =0
num2 =0

resultado=0

while opcao!= 0:
    opcao = exibirMenu()
    if opcao <=0:
        print("Saindo..")
        break
    elif opcao == 1:
        num1 = float(input("Informe o primeiro numero: "))
        num2 = float(input("Informe o segundo numero: "))
        resultado = somar(num1, num2)
        print("Resultado: %f\n\n " %resultado)
    elif opcao == 2:
        num1 = float(input("Informe o primeiro numero: "))
        num2 = float(input("Informe o segundo numero: "))
        resultado = sub(num1, num2)
        print("Resultado: %f\n\n " %resultado)
    elif opcao == 3:
        num1 = float(input("Informe o primeiro numero: "))
        num2 = float(input("Informe o segundo numero: "))
        resultado = mult(num1, num2)
        print("Resultado: %f\n\n " %resultado)
    elif opcao == 4:
        num1 = float(input("Informe o primeiro numero: "))
        num2 = float(input("Informe o segundo numero: "))
        resultado = div(num1, num2)
        print("Resultado: %f\n\n " %resultado)
    else:
        print("Digite uma opção valida!")
    