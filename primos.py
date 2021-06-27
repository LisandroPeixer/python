import os

os.system("clear")

num = int(input('Deseja saber os numeros primos de 2 ate quanto? '))

lista = []

def num_primo(num):
	tot_divisores = 0
	c = 1
	
	while c < num + 1:
		if num % c == 0:
			tot_divisores += 1
		c += 1
	
	if tot_divisores > 2:
		return False
	else:
		return True


for n in range(2, num):
	if num_primo(n):
		lista.append(n)


for n in lista:
	print(n)
