import os
import random
os.system("clear")
numero = random.randrange(0,10)
adivinhe = int( input(" digite um numero de 0 a 9: "))

while True:
    if adivinhe == numero:
        print("acertou")
        break
    else:
        adivinhe = int( input( "errou, tente denovo: "))

