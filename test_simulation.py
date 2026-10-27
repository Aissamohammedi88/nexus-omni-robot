#!/usr/bin/env python3
"""
Test simulation — Robot virtuel dans PyBullet
"""
import pybullet as p
import pybullet_data
import time

print("🤖 Démarrage de la simulation...")
p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.81)

# Sol
plane = p.loadURDF("plane.urdf")

# Robot simple (remplace par ton URDF plus tard)
robot = p.loadURDF("r2d2.urdf", [0, 0, 1])

print("✅ Simulation lancée. Le robot est dans la fenêtre.")
print(" Ferme la fenêtre pour arrêter.")

try:
while True:
p.stepSimulation()
time.sleep(1./240.)
except KeyboardInterrupt:
print("\n👋 Simulation arrêtée.")
p.disconnect()
