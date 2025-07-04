import math
oposto = float(input("Oposto: "))
adjascente = float(input("Adjascente: "))
hipotenusa =  math.sqrt(math.exp2(adjascente) + math.exp2(oposto))
print("Hipotenusa = {}, \nsen = {}, \ncos = {}, \ntan = {}".format(hipotenusa, oposto/hipotenusa, adjascente/hipotenusa, oposto/adjascente))