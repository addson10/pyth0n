n1 = int(input("digite o seu primeiro numero intero"))
n2 = int(input("digite o seu segundo numero intero"))
n3 = int(input("digite o seu terceiro numero intero"))
maior = max(n1, n2, n3)
menor = min(n1, n2, n3)
medio = n1 + n2 + n3 - maior - menor
print("valores em ordem decrescente:" , maior, medio, menor)