import socket
import network

ssid = 'NomDuWifi'
password = 'MotDePasse'

ap_if = network.WLAN(network.AP_IF)
ap_if.config(essid=ssid, password=password)
ap_if.active(True)

sock = socket.socket()
sock.bind(('0.0.0.0', 1234))
sock.listen(1)

conn, addr = sock.accept()
print('Client connecté de', addr)

while True:
    data = conn.recv(1024)
    if data:
        print('Commande reçue :', data)
        # exécuter action : par ex. avancer
