def verifica(aux):
    sc = init
    for i in  aux:
        ok = 0
        for j in lista_tranzitii:
            if j[0]  ==  sc and j[1] == i :
                    sc = j[2]
                    ok = 1
                    break
        if ok == 0:
            return False
    if sc in final:
        return True
    return False

with open("citire1.txt", "r") as f:
    g = open("afisare.txt", "w")
    n = int(f.readline()) # n = numar de stari
    m = int(f.readline()) # m = numar de caractere din alfabet

    alfabet = [i for i in f.readline().split()] # alfabetul
    init = f.readline().strip() # starea initiala
    k = int(f.readline()) # k = numar de stari finale

    final = [x for x in f.readline().split()] # starile finale
    l = int(f.readline()) # l = numar de tranzitii

    lista_tranzitii = []

    for i in range(l):
        linie = f.readline()
        linie = linie.split()
        lista_tranzitii.append([linie[0],linie[1],linie[2]])

    test = f.readline()

    if verifica(test) == True:
        print("true")
    else:
        print("false")

