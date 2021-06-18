#!/bin/bash

echo "Seja Bem-Vindo(a)"

op=1
while [  $op -ne 0 ]; do
    echo "Informe um numero"
        read n1
    echo "Informe um numero"
        read n2

echo "Escolha uma operação"
echo "1 - Adição"
echo "2 - Subtração"
echo "3 - Multiplicação"
echo "4 - Divisão"
 read op

if [ $op -eq 1 ];
then
    resultado=$[n1+n2]
    echo "Resultado $resultado"
elif [ $op -eq 2 ]
then
    resultado=$[n1-n2]
    echo "Resultado $resultado"
elif [ $op -eq 3 ]
then
    resultado=$[n1*n2]
    echo "Resultado $resultado"
elif [ $op -eq 4 ]
then
    resultado=$[n1/n2]
    echo "Resultado $resultado"
else
    echo "Opção invalida!"
fi
done












