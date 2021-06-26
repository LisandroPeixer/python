#um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#faça um programa que ajude ele , lendo o nome deles e escrevendo o nome do escolhido.

import os
import random

os.system("clear")
n1= str(input('primeiro aluno:'))
n2= str(input('segundo aluno:'))
n3= str(input('terceiro aluno:'))
n4= str(input('quarto aluno:'))
lista = [n1 , n2 , n3 , n4]
escolhido=random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
