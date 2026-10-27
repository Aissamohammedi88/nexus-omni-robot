#!/usr/bin/env python3
"""
Test vocal — Parle à ton robot via ton casque
"""
import json
import queue
import sys
import sounddevice as sd
from vosk import Model, KaldiRecognizer

MODEL_PATH = "models/vosk-model-fr"
SAMPLE_RATE = 16000

print("🔊 Chargement du modèle vocal...")
model = Model(MODEL_PATH)
recognizer = KaldiRecognizer(model, SAMPLE_RATE)

q = queue.Queue()

def callback(indata, frames, time, status):
if status:
print(status, file=sys.stderr)
q.put(bytes(indata))

print("🎤 Parle maintenant (Ctrl+C pour arrêter)...")
print("Commandes test : avance, recule, stop, tourne\n")

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
texte = result.get("text", "")
if texte:
print(f"📝 Reçu : {texte}")
# Ici tu envoies la commande au robot
# Ex: envoyer_commande(texte)
else:
partial = json.loads(recognizer.PartialResult())
if partial.get("partial"):
print(f"⏳ ... {partial['partial']}", end="\r")

except KeyboardInterrupt:
print("\n👋 Arrêt du test vocal.")
