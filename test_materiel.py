#!/usr/bin/env python3
"""
Test matériel — Vérifie les composants connectés
"""
import serial
import serial.tools.list_ports

print("🔌 Ports série détectés :")
ports = serial.tools.list_ports.comports()

if not ports:
    print("   ❌ Aucun port série détecté.")
else:
    for port in ports:
        print(f"   ✅ {port.device} — {port.description}")

print("\n🎤 Périphériques audio :")
try:
    import sounddevice as sd
    devices = sd.query_devices()
    for i, dev in enumerate(devices):
        print(f"   [{i}] {dev['name']} — entrées: {dev['max_input_channels']}")
except Exception as e:
    print(f"   ⚠️ Erreur audio : {e}")

print("\n💡 Test terminé.")
