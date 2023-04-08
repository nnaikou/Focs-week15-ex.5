
def haeJoukot8(l1,l2,l3,l4,l5,l6,l7,l8,summa):
    checker = 0 #tarkistetaan tällä löytykö yhtäkään joukkoa
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    for m in range(2):
                        for n in range(2):
                            for o in range(2):
                                for p in range(2):
                                    if l1[i]+l2[j]+l3[k]+l4[l]+l5[m]+l6[n]+l7[o]+l8[p]==summa:
                                        checker = 1
                                        print("\nLöytyi joukko:  {",l1[i],l2[j],l3[k],l4[l],l5[m],l6[n],l7[o],l8[p],"}")
    if checker == 0:
        print("Ei löytynyt yhtäkään joukkoa")

def haeJoukot7(l1,l2,l3,l4,l5,l6,l7,summa):
    checker = 0 #tarkistetaan tällä löytykö yhtäkään joukkoa
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    for m in range(2):
                        for n in range(2):
                            for o in range(2):
                                if l1[i]+l2[j]+l3[k]+l4[l]+l5[m]+l6[n]+l7[o]==summa:
                                    checker = 1
                                    print("\nLöytyi joukko:  {",l1[i],l2[j],l3[k],l4[l],l5[m],l6[n],l7[o],"}")
    if checker == 0:
        print("Ei löytynyt yhtäkään joukkoa")

def haeJoukot6(l1,l2,l3,l4,l5,l6,summa):
    checker = 0 #tarkistetaan tällä löytykö yhtäkään joukkoa
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    for m in range(2):
                        for n in range(2):
                            if l1[i]+l2[j]+l3[k]+l4[l]+l5[m]+l6[n]==summa:
                                checker = 1
                                print("\nLöytyi joukko:  {",l1[i],l2[j],l3[k],l4[l],l5[m],l6[n],"}")
    if checker == 0:
        print("Ei löytynyt yhtäkään joukkoa")

def haeJoukot5(l1,l2,l3,l4,l5,summa):
    checker = 0 #tarkistetaan tällä löytykö yhtäkään joukkoa
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    for m in range(2):
                        if l1[i]+l2[j]+l3[k]+l4[l]+l5[m]==summa:
                            checker = 1
                            print("\nLöytyi joukko:  {",l1[i],l2[j],l3[k],l4[l],l5[m],"}")
    if checker == 0:
        print("Ei löytynyt yhtäkään joukkoa")

def haeJoukot4(l1,l2,l3,l4,summa):
    checker = 0 #tarkistetaan tällä löytykö yhtäkään joukkoa
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    if l1[i]+l2[j]+l3[k]+l4[l]==summa:
                        checker = 1
                        print("\nLöytyi joukko:  {",l1[i],l2[j],l3[k],l4[l],"}")
    if checker == 0:
        print("Ei löytynyt yhtäkään joukkoa")

def haeJoukot3(l1,l2,l3,summa):
    checker = 0 #tarkistetaan tällä löytykö yhtäkään joukkoa
    for i in range(2):
        for j in range(2):
            for k in range(2):
                if l1[i]+l2[j]+l3[k]==summa:
                    checker = 1
                    print("\nLöytyi joukko:  {",l1[i],l2[j],l3[k],"}")
    if checker == 0:
        print("Ei löytynyt yhtäkään joukkoa")

def haeJoukot2(l1,l2,summa):
    checker = 0 #tarkistetaan tällä löytykö yhtäkään joukkoa
    for i in range(2):
        for j in range(2):
            if l1[i]+l2[j]==summa:
                checker = 1
                print("\nLöytyi joukko:  {",l1[i],l2[j],"}")
    if checker == 0:
        print("Ei löytynyt yhtäkään joukkoa")

def haeJoukot1(l1,summa):
    checker = 0 #tarkistetaan tällä löytykö yhtäkään joukkoa
    for i in range(2):
        if l1[i]==summa:
            checker = 1
            print("\nLöytyi joukko:  {",l1[i],"}")
    if checker == 0:
        print("Ei löytynyt yhtäkään joukkoa")





def paaohjelma():
    vektorinKoko = int(input("Anna vektorin koko (max 8): "))
    summa = int(input("Anna etsittävä summa: "))

    while(True):
        askeltaja = 0
        l1 = [int(input("Anna vektorin alkiolle arvo: ")),0]
        askeltaja+=1
        if (askeltaja == vektorinKoko):
            haeJoukot1(l1,summa)
            break

        l2 = [int(input("Anna vektorin alkiolle arvo: ")),0]
        askeltaja+=1
        if (askeltaja == vektorinKoko):
            haeJoukot2(l1,l2,summa)
            break
        
        l3 = [int(input("Anna vektorin alkiolle arvo: ")),0]
        askeltaja+=1
        if (askeltaja == vektorinKoko):
            haeJoukot3(l1,l2,l3,summa)
            break
        
        l4 = [int(input("Anna vektorin alkiolle arvo: ")),0]
        askeltaja+=1
        if (askeltaja == vektorinKoko):
            haeJoukot4(l1,l2,l3,l4,summa)
            break
        
        l5 = [int(input("Anna vektorin alkiolle arvo: ")),0]
        askeltaja+=1
        if (askeltaja == vektorinKoko):
            haeJoukot5(l1,l2,l3,l4,l5,summa)
            break
        
        l6 = [int(input("Anna vektorin alkiolle arvo: ")),0]
        askeltaja+=1
        if (askeltaja == vektorinKoko):
            haeJoukot6(l1,l2,l3,l4,l5,l6,summa)
            break
        
        l7 = [int(input("Anna vektorin alkiolle arvo: ")),0]
        askeltaja+=1
        if (askeltaja == vektorinKoko):
            haeJoukot7(l1,l2,l3,l4,l5,l6,l7,summa)
            break
        
        l8 = [int(input("Anna vektorin alkiolle arvo: ")),0]
        askeltaja+=1
        if (askeltaja == vektorinKoko):
            haeJoukot8(l1,l2,l3,l4,l5,l6,l7,l8,summa)
            break
    
    print("\nKiitos ohjelman käytöstä.")

paaohjelma()
