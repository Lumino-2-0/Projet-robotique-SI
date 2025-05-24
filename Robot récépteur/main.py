from Servo_pince import Servo
from Moteur_controles import Moteur
import socket
import time

# Initialisation de la pince
pince = Servo(pin=5)

# Initialisation des moteurs
moteur_gauche = Moteur(ena=27, in1=7, in2=6)
moteur_droit = Moteur(ena=26, in1=18, in2=19)

# Configuration serveur WiFi
PORT = 1234
sock = socket.socket()
sock.bind(('0.0.0.0', PORT))
sock.listen(1)
print("Attente de connexion...")
conn, addr = sock.accept()
print("Connecté depuis", addr)

def arreter():
    moteur_gauche.stop()
    moteur_droit.stop()

while True:
    try:
        data = conn.recv(1024)
        if data:
            cmd = data.decode().strip().upper()
            print("Commande reçue :", cmd)

            if cmd == "AVANCER":
                moteur_gauche.avancer()
                moteur_droit.avancer()
            elif cmd == "RECULER":
                moteur_gauche.reculer()
                moteur_droit.reculer()
            elif cmd == "STOP":
                arreter()
            elif cmd == "PINCE_OUVRIR":
                pince.tourner(0)
            elif cmd == "PINCE_FERMER":
                pince.tourner(120)
            else:
                print("Commande inconnue.")
    except Exception as e:
        print("Erreur :", e)
        break

# Nettoyage
conn.close()
sock.close()
