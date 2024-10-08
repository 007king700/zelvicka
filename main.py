from zelva import *
shape("turtle")
while True:
    speed(0)
    while True:
        vstup = textinput("Výběr", "1 - Spirála\n2 - Kruh\n3 - Čtverec\n4 - Trojúhelník\n5 - Pětiúhelník\n6 - Smaž plátno\n0 - Konec")
        if vstup not in ["1", "2", "3", "4", "5", "6", "0"]:
            print("Neplatný vstup")
        else:
            break
    if vstup == "1":
        spirala()
    elif vstup == "2":
        kruh()
    elif vstup == "3":
        ctverec()
    elif vstup == "4":
        trojuhelnik()
    elif vstup == "5":
        petiuhelnik()
    elif vstup == "6":
        clear()
    else:
        break