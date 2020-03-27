def testare_NFA(test, i, stare):
    if i == len(test):
        if stare in final:
            return True
        return False
    c = test[i]
    dict_verificare = dict_tranzitii.get(stare)
    if dict_verificare:
        if dict_verificare.get(c):
            for k in dict_verificare[c]:
                if testare_NFA(test, i+1, k):
                    return True
        if dict_verificare.get('$'):
            for k in dict_verificare['$']:
                if testare_NFA(test,i,k):
                    return True
    return False

with  open("citire.txt", "r") as f:
    g = open("afisare.txt", "w")
    n = int(f.readline()) # n = numar de stari
    m = int(f.readline()) # m = numar de caractere din alfabet
    alfabet = ['$'].extend(f.readline().split()) # alfabetul
    init = int(f.readline())# starea initiala
    k = int(f.readline()) # k = numar de stari finale
    final = [int(x) for x in f.readline().split()] # starile finale
    l = int(f.readline()) # l = numar de tranzitii

    dict_tranzitii = {}

    #implementez un nested dictionary in care voi pune tuplurile din citire
    for i in range(l):
        c1, c2, c3 = f.readline().split()
        c1 = int(c1)
        c3 = int(c3)
        if dict_tranzitii.get(c1):
            c_urm = dict_tranzitii[c1].get(c2)
            if c_urm:
                dict_tranzitii[c1][c2].append(c3) # imi da eroare daca nu pun list in fata


            else:
                dict_tranzitii[c1][c2] = [c3]
                print(dict_tranzitii)

        else:
            dict_tranzitii.update({c1 : {c2 : [c3]}})


    test = f.readline()
    print(testare_NFA(test,0,init)) #din pacate, imi da false la toate testele.




