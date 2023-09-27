peso = float(input("digite seu peso"))
altura = float(input("digite sua altura"))
imc = peso / (altura**2)
if imc < 16:
    print("desnutrição grave", (imc,1))
elif imc <=16.9:
    print("desnutrição moderada", (imc,1))
elif imc <=18.4:
    print("desnutrição leve", (imc,1))
elif imc <=24.9:
    print("normal", (imc,1))
elif imc <=29.9:
    print("sobrepeso", (imc,1))
elif imc <=34.9:
    print("obesidade 1° grau", (imc,1))
elif imc <=39.9:
    print("obesidade 2° grau", (imc,1))
else:
    print("obesidade 3° grau", (imc,1))