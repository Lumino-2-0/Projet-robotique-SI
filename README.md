# Projet-robotique-SI
# Télécommande WiFi avec Joystick pour Raspberry Pi Pico W

Ce code à pour but d'aider des étudiants sur un projet lycéen de première général en S.I !

## Objectif

Ce projet permet de piloter un robot à distance à l’aide :
- d’une carte **Raspberry Pi Pico W**
- d’un **joystick analogique Grove**
- et d’un **bouton poussoir**.

La carte agit comme une **télécommande sans fil**, en envoyant des commandes au robot via **WiFi** (protocole TCP/IP).

---

## Fonctionnement général

Le code lit en continu les valeurs analogiques des axes X et Y du joystick, détecte l’appui sur un bouton pour commander la pince, et envoie des **commandes textuelles** à une seconde carte Pico W (robot récepteur).

Les commandes envoyées peuvent être :
- `AVANCER`
- `RECULER`
- `STOP`
- `PINCE_OUVRIR`
- `PINCE_FERMER`

---

## Connexion réseau

Le programme utilise les éléments suivants pour se connecter au réseau local :

```python
ssid = 'TON_WIFI'
password = 'TON_MDP'
robot_ip = '192.168.1.50'
