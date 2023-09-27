al = float(input("digite sua altura"))
sex = str(input("digite seu sexo"))
if sex == "masculino" or sex == "Masculino" or sex == "MASCULINO":
    calc = (72.7 * al) - 58
    print("seu peso ideal é:", round(calc , 1))
elif sex == "feminino" or sex == "Feminino" or sex == "FEMININO":
    calc_2 = (62.1 * al) - 44.7
    print("seu peso ideal é:", round(calc_2 , 1))