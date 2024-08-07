numero = int(input("Digite um número natural: "))

fatorial = 1
i = 1
while i <= numero:
    fatorial *= i
    i += 1

print(fatorial)