from machine import Pin
from time import sleep

# Exemple pour le codeur gauche
c1 = Pin(8, Pin.IN)
c2 = Pin(9, Pin.IN)

compteur = 0
etat_prec = c1.value()

while True:
    etat = c1.value()
    if etat != etat_prec:
        if c2.value() != etat:
            compteur += 1
        else:
            compteur -= 1
        print("Impulsions : ", compteur)
        etat_prec = etat
    sleep(0.001)
