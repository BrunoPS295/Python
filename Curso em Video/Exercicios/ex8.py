#Detector de vogais
word = str(input("Digite uma palavra: ")).lower()
vogais = ("a","e","i","o","u")
aeiou = []
none = 0

for i in range(5):
    list = word.count(vogais[i])
    none += list
    aeiou.append(list)
    list = 0

ver = [
    f"\n{aeiou[0]}A" if aeiou[0] != 0 else "",
    f"\n{aeiou[1]}E" if aeiou[1] != 0 else "",
    f"\n{aeiou[2]}I" if aeiou[2] != 0 else "",
    f"\n{aeiou[3]}O" if aeiou[3] != 0 else "",
    f"\n{aeiou[4]}U" if aeiou[4] != 0 else ""
    ]

res = "Na palavra {} tem {} {} {} {} {}" .format(word, ver[0], ver[1], ver[2], ver[3], ver[4])
if none == 0:
    print("Não há vogais")
else:
    print(res)

