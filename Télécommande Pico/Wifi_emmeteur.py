import socket
import network
import time
from machine import ADC, Pin

ssid = 'NomSSID' # Nom du réseau Wi-Fi
password = 'MDP'  # Mot de passe du réseau Wi-Fi
robot_ip = '192.168.1.50' # Adresse IP du robot

# Init WiFi
sta_if = network.WLAN(network.STA_IF) # Mode station (client)
sta_if.active(True) 
sta_if.connect(ssid, password) 

while not sta_if.isconnected():  # Attente de connexion
    print("Connexion en cours...")
    time.sleep(1)
print("Connecté :", sta_if.ifconfig()) # Affiche l'IP, le masque, la passerelle et le DNS

# Connexion au robot
sock = socket.socket() # Création du socket
sock.connect((robot_ip, 1234)) # Connexion au port du robot
print("Connecté au robot")

# Joystick analogique
joy_x = ADC(Pin(26))  # Axe horizontal 
joy_y = ADC(Pin(27))  # Axe vertical
btn = Pin(15, Pin.IN, Pin.PULL_UP)  # Bouton pour pince

# Fonctions utilitaires
def lire_joystick(): 
    x = joy_x.read_u16() # Lecture de l'axe horizontal avec une résolution de 16 bits
    y = joy_y.read_u16() # Lecture de l'axe vertical avec une résolution de 16 bits
    return x, y

def envoyer(cmd):
    print("Envoi :", cmd) # Affiche la commande envoyée
    sock.send(cmd.encode()) # Envoie la commande au robot

# Main loop
etat_pince = False  # False = ouverte, True = fermée
derniere_cmd = ""   # Pour éviter les répétitions de commandes

while True:
    x, y = lire_joystick() # Lecture des valeurs du joystick

    # Détection mouvements
    if y > 50000: # Si le joystick est poussé vers le haut
        cmd = "AVANCER"
    elif y < 15000: # Si le joystick est poussé vers le bas
        cmd = "RECULER"
    elif x > 50000: # Si le joystick est poussé vers la droite
        cmd = "DROITE"  # Optionnel
    elif x < 15000: # Si le joystick est poussé vers la gauche
        cmd = "GAUCHE"  # Optionnel
    else:
        cmd = "STOP"

    # Éviter les répétitions
    if cmd != derniere_cmd:
        envoyer(cmd)
        derniere_cmd = cmd

    # Bouton pince
    if not btn.value():  # Bouton appuyé
        time.sleep(0.3)  # anti-rebond
        if not etat_pince: # Si la pince est ouverte
            envoyer("PINCE_FERMER")
            etat_pince = True
        else:
            envoyer("PINCE_OUVRIR")
            etat_pince = False

    time.sleep(0.1)