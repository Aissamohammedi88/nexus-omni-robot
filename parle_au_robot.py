#!/usr/bin/env python3
"""
CONVERSATION DIRECTE — Parle au robot
Reconnaissance vocale + réponse vocale + action
"""
import json
import queue
import sys
import os
import subprocess
import time

from vosk import Model, KaldiRecognizer
import sounddevice as sd

MODEL_PATH = "models/vosk-model-fr"
SAMPLE_RATE = 16000

if not os.path.exists(MODEL_PATH):
    print(f"❌ Modèle introuvable : {MODEL_PATH}")
    sys.exit(1)

print("=" * 60)
print("🤖 ROBOT EN ÉCOUTE — Parle maintenant")
print("=" * 60)

model = Model(MODEL_PATH)
recognizer = KaldiRecognizer(model, SAMPLE_RATE)
q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

# Réponses du robot
REPONSES = {
    "bonjour": "Bonjour. Je suis opérationnel. Je t'écoute.",
    "ça va": "Je fonctionne correctement. Tous mes systèmes sont verts.",
    "avance": "J'avance.",
    "recule": "Je recule.",
    "stop": "Arrêt immédiat.",
    "tourne": "Je tourne.",
    "gauche": "Je tourne à gauche.",
    "droite": "Je tourne à droite.",
    "qui es tu": "Je suis ton robot. Construit par toi. Je t'obéis.",
    "merci": "Avec plaisir.",
}

def parler(texte):
    """Fait parler le robot avec espeak"""
    try:
        subprocess.run(["espeak", "-v", "fr", "-s", "150", texte],
                       check=False, timeout=5)
    except Exception:
        print(f"   (voix indisponible) → {texte}")

print("\n🎤 Je t'écoute. Parle (Ctrl+C pour arrêter).\n")

try:
    with sd.RawInputStream(
        samplerate=SAMPLE_RATE,
        blocksize=8000,
        device=None,
        dtype='int16',
        channels=1,
        callback=callback
    ):
        while True:
            data = q.get()
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                texte = result.get("text", "").lower().strip()
                if texte:
                    print(f"👤 Toi : {texte}")
                    
                    # Chercher une réponse
                    reponse = None
                    for cle, val in REPONSES.items():
                        if cle in texte:
                            reponse = val
                            break
                    
                    if reponse is None:
                        reponse = f"J'ai entendu : {texte}. Commande inconnue."
                    
                    print(f"🤖 Robot : {reponse}")
                    parler(reponse)
                    print()
            else:
                partial = json.loads(recognizer.PartialResult())
                if partial.get("partial"):
                    print(f"⏳ {partial['partial']}", end="\r")

except KeyboardInterrupt:
    print("\n\n👋 Conversation terminée.")
