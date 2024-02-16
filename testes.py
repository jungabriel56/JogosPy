import random

a = "junga"

b = "papa"

print(a,b, sep="-")

print("Tentativa {:07.2f} de {:.2f}".format(3.1,10.12))
print("Tentativa {1} de {0}".format(3,10))
print("Data {:02d}/{:07d}".format(9,4))

print(random.seed(100))

frase = "Olá, mundo!"

for i in range(len(frase)):
    print("O caractere na posição", i, "é", frase[i])

passos = 0
while (passos < 9):
    passos += 1
print(passos)