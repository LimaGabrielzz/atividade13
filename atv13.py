# Exercício Python 14: Faça um programa que leia três números e
# mostre qual é o maior e qual é o menor.
n1 = int(input("digite um número: "))
n2 = int(input("digite um número: "))
n3 = int(input("digite um número: "))
if n1 > n2 and n3:
    print(f"O maior numero é {n1}")
elif n2 > n1 and n3:
    print(f"O maior numero é {n2}")
else:
    print(f"O maior numero é {n3}")
if n1 < n2 and n3:
    print(f"O menor numero é {n1}")
elif n2 < n1 and n3:
    print(f"O menor numero é {n2}")
else:
    print(f"O menor numero é {n3}")