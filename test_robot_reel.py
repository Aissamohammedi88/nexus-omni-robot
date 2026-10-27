#!/usr/bin/env python3
"""
TEST RÉEL DU ROBOT
Détecte, mesure, et rapporte l'état réel du système.
"""
import os
import sys
import time
import subprocess

print("=" * 60)
print("🤖 TEST RÉEL DU ROBOT")
print("=" * 60)

# --- 1. DÉTECTION DU ROBOT (USB) ---
print("\n[1/5] 🔌 DÉTECTION USB")
try:
    import serial.tools.list_ports
    ports = list(serial.tools.list_ports.comports())
    robot_ports = [p for p in ports if 'ttyUSB' in p.device or 'ttyACM' in p.device]
    
    if robot_ports:
        for p in robot_ports:
            print(f"   ✅ ROBOT DÉTECTÉ : {p.device}")
            print(f"      Description : {p.description}")
            print(f"      Fabricant  : {p.manufacturer}")
            print(f"      VID:PID    : {p.vid}:{p.pid}")
    else:
        print("   ❌ AUCUN ROBOT DÉTECTÉ en USB")
        print("   → Branche ton Arduino/ESP32 en USB")
except Exception as e:
    print(f"   ⚠️ Erreur : {e}")

# --- 2. DÉTECTION AUDIO ---
print("\n[2/5] 🎤 DÉTECTION AUDIO")
try:
    import sounddevice as sd
    devices = sd.query_devices()
    input_devices = []
    for i, dev in enumerate(devices):
        if dev['max_input_channels'] > 0:
            input_devices.append((i, dev['name'], dev['max_input_channels']))
    
    if input_devices:
        print(f"   ✅ {len(input_devices)} périphérique(s) d'entrée détecté(s) :")
        for i, name, ch in input_devices:
            print(f"      [{i}] {name} ({ch} canaux)")
    else:
        print("   ❌ Aucun micro détecté")
except Exception as e:
    print(f"   ⚠️ Erreur : {e}")

# --- 3. TEST CPU / MÉMOIRE ---
print("\n[3/5] 💻 RESSOURCES SYSTÈME")
try:
    import psutil
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
    print(f"   CPU    : {cpu}% utilisé")
    print(f"   RAM    : {mem.percent}% utilisé ({mem.used // (1024**2)} MB / {mem.total // (1024**2)} MB)")
    print(f"   Disque : {disk.percent}% utilisé")
except ImportError:
    print("   ⚠️ psutil non installé. Installation...")
    subprocess.run([sys.executable, "-m", "pip", "install", "psutil"])
except Exception as e:
    print(f"   ⚠️ Erreur : {e}")

# --- 4. TEST BATTERIE (si laptop) ---
print("\n[4/5] 🔋 BATTERIE")
try:
    import psutil
    batt = psutil.sensors_battery()
    if batt:
        print(f"   Niveau    : {batt.percent}%")
        print(f"   Branché   : {'Oui' if batt.power_plugged else 'Non'}")
    else:
        print("   ⚠️ Pas de batterie détectée (PC fixe ?)")
except Exception as e:
    print(f"   ⚠️ Erreur : {e}")

# --- 5. TEST COMMUNICATION SÉRIE (si robot branché) ---
print("\n[5/5] 📡 TEST COMMUNICATION SÉRIE")
try:
    import serial
    import serial.tools.list_ports
    
    ports = [p.device for p in serial.tools.list_ports.comports() 
             if 'ttyUSB' in p.device or 'ttyACM' in p.device]
    
    if ports:
        port = ports[0]
        print(f"   Test sur {port}...")
        ser = serial.Serial(port, 115200, timeout=2)
        time.sleep(2)
        ser.write(b"PING\n")
        time.sleep(1)
        response = ser.read_all()
        ser.close()
        
        if response:
            print(f"   ✅ RÉPONSE DU ROBOT : {response.decode('utf-8', errors='ignore').strip()}")
        else:
            print("   ⚠️ Aucune réponse. Le robot est-il allumé ?")
    else:
        print("   ❌ Aucun port série robot. Branche ton Arduino/ESP32.")
except Exception as e:
    print(f"   ⚠️ Erreur : {e}")

# --- RÉSUMÉ ---
print("\n" + "=" * 60)
print("📊 RÉSUMÉ")
print("=" * 60)
print("\n→ Si un test échoue, corrige AVANT de continuer.")
print("→ Si tout passe, le robot est prêt pour le test vocal.\n")
