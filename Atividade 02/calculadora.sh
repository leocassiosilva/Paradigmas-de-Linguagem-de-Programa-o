#!/bin/bash

if ['/home/leocassio/shell/DirShell01' && '/home/leocassio/shell/DirShell02']
then echo "O diretorio já existe"
else 
mkdir DirShell01
mkdir DirShell02
fi 

python calculadora.py 

mv /home/leocassio/shell/DirShell01/lista.txt -t /home/leocassio/shell/DirShell02