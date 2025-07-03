print("1 pessoa")
I_n = input("Nome: ")
I_i = int(input("Idade: "))
I_s = input("Sexo: ")

print("2 pessoa")
II_n = input("Nome: ")
II_i = int(input("Idade: "))
II_s = input("Sexo: ")

print("3 pessoa")
III_n = input("Nome: ")
III_i = int(input("Idade: "))
III_s = input("Sexo: ")

print("4 pessoa")
IV_n = input("Nome: ")
IV_i = int(input("Idade: "))
IV_s = input("Sexo: ")

media_i = (I_i + II_i + III_i + IV_i) / 4
velho = 0
velho_i = "x"
muie = 0
key = 0

print("Média idade: {}" .format(media_i))

if I_i > II_i and I_i > III_i and I_i > IV_i and I_s == "m":
    velho = I_n
    velho_i = I_i
elif II_i > I_i and II_i > III_i and II_i > IV_i and II_s == "m":
    velho = II_n
    velho_i = II_i
elif III_i > I_i and III_i > II_i and III_i > IV_i and III_s == "m":
    velho = III_n
    velho_i = III_i
elif IV_i > I_i and IV_i > II_i and IV_i > III_i and IV_s == "m":
    velho = IV_n
    velho_i = IV_i
else:
    key+=1

if key == 0:
    print("O homi mais velho é o {} com {} anos".format(velho, velho_i))
else:
    print("Só tem muié")

if I_i < 20 and I_s == "f":
    muie+=1
if II_i < 20 and II_s == "f":
    muie+=1
if III_i < 20 and III_s == "f":
    muie+=1
if IV_i < 20 and IV_s == "f":
    muie+=1

if muie != 0:
    print("Tem {} mulheres com menos de 20".format(muie))
else:
    print("Só veia")





