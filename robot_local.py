#!/usr/bin/env python3
"""
ROBOT LOCAL — Whisper + Piper
100% hors-ligne. Aucune clé API.
"""
import os
import subprocess
import tempfile
import sys

import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

# Chemins
PIPER_MODEL = "voices/fr_FR-siwis-medium.onnx"
SAMPLE_RATE = 16000
DUREE = 4

print("=" * 60)
print("🤖 ROBOT — FORGERON NEXUS")
print("=" * 60)

# Vérifier le modèle Piper
if not os.path.exists(PIPER_MODEL):
print(f"❌ Modèle Piper introuvable : {PIPER_MODEL}")
sys.exit(1)
print("✅ Piper prêt")

# Charger Whisper
print("📥 Chargement de Whisper (patienter 10-20s)...")
from faster_whisper import WhisperModel
model = WhisperModel("small", device="cpu", compute_type="int8")
print("✅ Whisper prêt")

# Intentions
INTENTIONS = {
"MOUVEMENT_AVANT": ["avance", "avancer", "va", "vas", "marche", "forward", "continue"],
"MOUVEMENT_ARRIERE": ["recule", "reculer", "arrière", "back", "retourne"],
"GAUCHE": ["gauche"],
"DROITE": ["droite"],
"ARRET": ["stop", "arrête", "arrêter", "halte", "pause", "fige"],
"LENT": ["doucement", "lentement", "lent", "calme", "prudent"],
"RAPIDE": ["vite", "rapide", "rapidement", "accélère", "fonce"],
"IDENTITE": ["qui", "es", "tu", "nom", "identité"],
"SALUTATION": ["bonjour", "salut", "hello", "coucou", "bonsoir"],
"MERCI": ["merci", "thanks"],
"AIDE": ["aide", "help", "commande", "peux", "faire"],
"ALLUME": ["allume", "éclaire", "led", "lumière"],
"ETEINS": ["éteins", "éteindre", "coupe", "off"],
"SCAN": ["détecte", "scan", "obstacle", "distance", "mesure"],
"BATTERIE": ["batterie", "charge", "énergie", "niveau"],
}

def enregistrer(duree=DUREE):
print(f"\n🎤 Enregistrement {duree}s...")
audio = sd.rec(int(duree * SAMPLE_RATE),
samplerate=SAMPLE_RATE,
channels=1, dtype='int16')
sd.wait()
return audio.flatten()

def transcrire(audio):
with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
wav.write(f.name, SAMPLE_RATE, audio)
segments, _ = model.transcribe(f.name, language="fr")
texte = " ".join([s.text for s in segments]).strip()
os.unlink(f.name)
return texte

def parler(texte):
with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
subprocess.run(["piper", "--model", PIPER_MODEL,
"--output_file", f.name],
input=texte.encode(), check=False)
subprocess.run(["aplay", f.name], check=False)
os.unlink(f.name)

def analyser(phrase):
phrase = phrase.lower().strip()
mots = phrase.split()
trouve = []
for intention, cles in INTENTIONS.items():
for cle in cles:
if cle in mots:
trouve.append(intention)
break
return trouve, mots

def repondre(intentions):
if "ARRET" in intentions:
return "Arrêt immédiat."
if "SALUTATION" in intentions:
return "Salut, je t'écoute."
if "MERCI" in intentions:
return "Avec plaisir, forgeron."
if "IDENTITE" in intentions:
return "Je suis ton robot. Forgé par toi."
if "AIDE" in intentions:
return "Dis : avance, recule, gauche, droite, stop, allume, éteins, scan."
if "BATTERIE" in intentions:
return "Niveau de batterie : nominal."
if "SCAN" in intentions:
return "Je scanne les environs."
if "ALLUME" in intentions:
return "J'allume la LED."
if "ETEINS" in intentions:
return "J'éteins la LED."
if "MOUVEMENT_AVANT" in intentions:
v = "lente" if "LENT" in intentions else ("rapide" if "RAPIDE" in intentions else "normale")
return f"J'avance à vitesse {v}."
if "MOUVEMENT_ARRIERE" in intentions:
v = "lente" if "LENT" in intentions else ("rapide" if "RAPIDE" in intentions else "normale")
return f"Je recule à vitesse {v}."
if "GAUCHE" in intentions:
return "Je tourne à gauche."
if "DROITE" in intentions:
return "Je tourne à droite."
return None

print("\n🎤 Parle maintenant (Ctrl+C pour arrêter)\n")

try:
while True:
audio = enregistrer(DUREE)
texte = transcrire(audio)

if not texte.strip():
print(" (silence)")
continue

print(f"👤 Toi : {texte}")
intentions, mots = analyser(texte)
print(f" Mots : {mots}")
print(f" Intentions : {intentions}")

reponse = repondre(intentions)
if reponse:
print(f"🤖 Robot : {reponse}\n")
parler(reponse)
else:
print(" (aucune intention reconnue)\n")

except KeyboardInterrupt:
print("\n👋 Arrêt.")
