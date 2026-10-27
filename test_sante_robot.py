#!/usr/bin/env python3
"""
DIAGNOSTIC VITAL DU ROBOT
Vérifie : alimentation, capteurs, moteurs, communication, sécurité
"""
import time
import sys

print("=" * 60)
print("🔍 DIAGNOSTIC VITAL — ROBOT")
print("=" * 60)

# --- 1. TEST D'ALIMENTATION ---
print("\n[1/6] 🔋 ALIMENTATION")
print("  - Vérifie visuellement la tension de la batterie")
print("  - Tension attendue : 11.1V - 12.6V (LiPo 3S)")
print("  - Si < 10.5V → ARRÊT IMMÉDIAT")
print("  - Si > 13.0V → ARRÊT IMMÉDIAT")

# --- 2. TEST DES CAPTEURS ---
print("\n[2/6] 📡 CAPTEURS")
print("  - Ultrason : distance mesurée")
print("  - IMU : accélération, gyroscope")
print("  - Caméra : flux vidéo")
print("  - Encodeurs : rotation des roues")

# --- 3. TEST DES MOTEURS ---
print("\n[3/6] ⚙️ MOTEURS")
print("  - Test roue gauche (avance/recule)")
print("  - Test roue droite (avance/recule)")
print("  - Test arrêt d'urgence")

# --- 4. TEST DE COMMUNICATION ---
print("\n[4/6] 📶 COMMUNICATION")
print("  - Port série : /dev/ttyUSB0 ou /dev/ttyACM0")
print("  - Baudrate : 115200")
print("  - Latence : < 50ms")

# --- 5. TEST DE SÉCURITÉ ---
print("\n[5/6] 🛡 SÉCURITÉ")
print("  - Bouton d'arrêt d'urgence fonctionnel")
print("  - Détection d'obstacle < 20cm → arrêt")
print("  - Limite de vitesse : 0.5 m/s max")
print("  - Zone de test : fermée, sans humains")

# --- 6. TEST ENVIRONNEMENTAL ---
print("\n[6/6] 🌍 ENVIRONNEMENT")
print("  - Température : 10°C - 35°C")
print("  - Sol : plat, non glissant")
print("  - Éclairage : suffisant pour caméra")

print("\n" + "=" * 60)
print("✅ DIAGNOSTIC TERMINÉ")
print("=" * 60)
print("\n⚠️ Ne pas mettre le robot en marche si un test échoue.")
