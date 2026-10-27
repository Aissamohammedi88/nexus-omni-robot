#!/usr/bin/env python3
"""
SIMULATION COMPLÈTE — Test du robot dans PyBullet
Aucun risque physique. Test de tous les comportements.
"""
import pybullet as p
import pybullet_data
import time

print("=" * 60)
print("🤖 SIMULATION ROBOT — PyBullet")
print("=" * 60)

# Connexion
p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.81)

# Sol
plane = p.loadURDF("plane.urdf")

# Robot (remplace par ton URDF)
robot = p.loadURDF("r2d2.urdf", [0, 0, 0.5])

print("\n✅ Simulation lancée")
print("   - Robot chargé")
print("   - Gravité activée")
print("   - Sol présent")
print("\n💡 Teste les mouvements dans la fenêtre.")
print("   Ferme la fenêtre pour arrêter.\n")

try:
    while True:
        p.stepSimulation()
        time.sleep(1./240.)
except KeyboardInterrupt:
    print("\n👋 Simulation arrêtée.")
    p.disconnect()
