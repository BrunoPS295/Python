boletim = []

while True:
    nome = str(input("Nome: "))
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    if n1 > 10 or n1 < 0 or n2 > 10 or n2 < 0:
         print("Erro, as notas devem receber um valor de 0 a 10")
    else:
        media = (n1 + n2) /2
        alunos = {"nome":nome, "nota1":n1, "nota2":n2, "media":media}
        boletim.append(alunos)
        sn = str(input("Continuar? [S/N]: ")).lower()
        if sn == "n": break

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print(f"No. Nome {"Média":>10}" )
print("---------------------------------------------------------------------")

for i in range(len(boletim)):
    dist = len(boletim[i]["nome"]) - 13
    print(f"{i}   {boletim[i]["nome"]}  {boletim[i]["media"]:>{dist}.1f}")
print("---------------------------------------------------------------------")

while True:
    sn2 = int(input("Mostrar qual nota? [-1 para parar]"))
    if sn2 == -1: 
        break
    elif sn2 > len(boletim) or sn2 < 0:
        print("Aluno não encontrado")
    else:
        print(f"Notas de {boletim[sn2]["nome"]} são [{boletim[sn2]["nota1"]:.1f}, {boletim[sn2]["nota2"]:.1f}]")
        print("---------------------------------------------------------------------")
print("<<< VOLTE SEMPRE >>>")
