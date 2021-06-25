file = open('/home/leocassio/Área de Trabalho/shell/DirShell01/lista.txt', 'w+')
num1 = 10
num2 = 2
opcao = 2

if opcao == 1:
   resultado = num1 + num2
   file.write(str(num1) + ' + ' + str(num2) + ' = ' + str(resultado))
elif opcao == 2:
    resultado = num1 - num2
    file.write(str(num1) + ' - ' + str(num2) + ' = ' + str(resultado))
elif opcao == 3:
    resultado = num1 * num2
    file.write(str(num1) + ' * ' + str(num2) + ' = ' + str(resultado))
    
elif opcao == 4:
    resultado = num1 / num2
    file.write(str(num1) + ' / ' + str(num2) + ' = ' + str(resultado))
else:
    file.write("OPÇÂO INVALIDA!")

file.close()

