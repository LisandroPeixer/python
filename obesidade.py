import os
os.system("clear")
print("calculando massa corporal")

peso = float( input("digite seu peso em kg (ex 70.0): "))
altura = float( input("digite sua altura em metro (ex 1.70): "))

imc = peso / (altura ** 2)
print("seu indice de massa corporal e: ", round(imc, 2))

if( imc <= 18.5):
    classificacao = "abaixo da media"
elif( imc > 18.5 and imc <= 24.9):
    classificacao = "dentro da media"
elif( imc > 24.9 and imc <= 29.9):
    classificacao = "acima da media"
else:
    classificacao = "obeso"

print("a classificacao de sua imc e: ", classificacao)
