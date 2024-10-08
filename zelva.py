from turtle import *
def kruh():
    for i in range(180):
        forward(2)
        left(2)
    
def ctverec():
    delka = textinput("Výběr","Zadej délku strany čtverce: ")
    for i in range(4):
        forward(int(delka))
        left(90)
    
def trojuhelnik():
    delka = textinput("Výběr","Zadej délku strany trojúhelníku: ")
    for i in range(3):
        forward(int(delka))
        left(120)
    
def petiuhelnik():
    delka = textinput("Výběr","Zadej délku strany pětiúhelníku: ")
    for i in range(5):
        forward(int(delka))
        left(72)
    
def spirala():
    pocet = textinput("Výběr","Zadej počet kruhů spirály: ")
    for i in range(int(pocet) * 10):
        forward(i)
        left(30)
    
