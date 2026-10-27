#!/usr/bin/env python3
"""
MOTEUR LOGIQUE DE DÉCOUPAGE
Découpe les mots, analyse, comprend l'intention
"""
import re
import unicodedata
from collections import Counter

# ============================================================
# NORMALISATION
# ============================================================
def normaliser(texte):
"""Enlève accents, met en minuscule, nettoie"""
texte = texte.lower()
texte = unicodedata.normalize('NFD', texte)
texte = ''.join(c for c in texte if unicodedata.category(c) != 'Mn')
texte = re.sub(r'[^\w\s]', ' ', texte)
return texte.strip()

def decouper(texte):
"""Découpe en mots"""
return re.findall(r'\b\w+\b', normaliser(texte))

# ============================================================
# STOPWORDS (mots vides à ignorer)
# ============================================================
STOPWORDS = {
"le", "la", "les", "un", "une", "des", "du", "de", "d",
"et", "ou", "mais", "donc", "or", "ni", "car",
"je", "tu", "il", "elle", "on", "nous", "vous", "ils", "elles",
"me", "te", "se", "moi", "toi", "lui", "leur",
"à", "au", "aux", "en", "dans", "sur", "sous", "avec", "sans",
"pour", "par", "vers", "chez", "entre",
"est", "sont", "été", "être", "avoir", "ai", "as", "a",
"ce", "cet", "cette", "ces", "ceci", "cela",
"que", "qui", "quoi", "dont", "où",
"y", "n", "ne", "pas", "plus", "moins",
}

def filtrer_mots(mots):
"""Garde seulement les mots porteurs de sens"""
return [m for m in mots if m not in STOPWORDS and len(m) > 1]

# ============================================================
# CATÉGORIES DE MOTS
# ============================================================
VERBES_ACTION = {
"avance", "avancer", "va", "vas", "marche", "continue", "poursuis",
"recule", "reculer", "retourne", "reviens",
"tourne", "pivote", "rotation", "oriente",
"arrete", "arreter", "stop", "halte", "pause", "fige", "immobilise",
"allume", "eclaire", "active",
"eteins", "eteindre", "coupe", "desactive",
"detecte", "scan", "mesure", "analyse", "observe",
"ouvre", "ferme", "attrape", "saisis", "lache",
"monte", "descend", "saute",
}

DIRECTIONS = {
"avant", "devant", "face",
"arriere", "derriere", "dos",
"gauche", "droite",
"haut", "bas",
"haut", "nord", "sud", "est", "ouest",
}

VITESSES = {
"doucement", "lentement", "lent", "calme", "prudent", "doux",
"vite", "rapide", "rapidement", "accelere", "fonce", "vitesse",
}

QUANTITES = {
"peu", "beaucoup", "tres", "trop", "assez", "plein",
"un", "deux", "trois", "quatre", "cinq",
}

TEMPS = {
"maintenant", "tout", "suite", "apres", "avant", "pendant",
"seconde", "minute", "heure", "moment",
}

NOMS = {
"led", "lumiere", "lampe", "moteur", "roue", "bras", "pince",
"batterie", "charge", "energie", "capteur", "camera", "micro",
"obstacle", "mur", "sol", "chemin", "route",
}

# ============================================================
# ANALYSE LOGIQUE
# ============================================================
def analyser(phrase):
"""
Analyse complète : découpe, catégorise, déduit l'intention
"""
mots_bruts = decouper(phrase)
mots = filtrer_mots(mots_bruts)

analyse = {
"phrase_originale": phrase,
"mots_bruts": mots_bruts,
"mots_filtres": mots,
"verbes": [],
"directions": [],
"vitesses": [],
"quantites": [],
"temps": [],
"noms": [],
"inconnus": [],
}

for mot in mots:
if mot in VERBES_ACTION:
analyse["verbes"].append(mot)
elif mot in DIRECTIONS:
analyse["directions"].append(mot)
elif mot in VITESSES:
analyse["vitesses"].append(mot)
elif mot in QUANTITES:
analyse["quantites"].append(mot)
elif mot in TEMPS:
analyse["temps"].append(mot)
elif mot in NOMS:
analyse["noms"].append(mot)
else:
analyse["inconnus"].append(mot)

# Déduire l'intention
analyse["intention"] = deduire_intention(analyse)

return analyse

def deduire_intention(analyse):
"""Déduit l'intention principale"""
if analyse["verbes"]:
return analyse["verbes"][0]
if analyse["noms"]:
return f"info_{analyse['noms'][0]}"
return "inconnu"

# ============================================================
# TEST
# ============================================================
if __name__ == "__main__":
exemples = [
"Avance doucement vers la droite",
"Stop tout de suite",
"Allume la lumière maintenant",
"Recule vite",
"Tourne à gauche lentement",
"Scanne les obstacles devant",
"Ouvre la pince et attrape",
"Qui es-tu ?",
]

for phrase in exemples:
resultat = analyser(phrase)
print(f"\n👤 {phrase}")
print(f" Mots bruts : {resultat['mots_bruts']}")
print(f" Mots filtrés : {resultat['mots_filtres']}")
print(f" Verbes : {resultat['verbes']}")
print(f" Directions : {resultat['directions']}")
print(f" Vitesses : {resultat['vitesses']}")
print(f" Noms : {resultat['noms']}")
print(f" Inconnus : {resultat['inconnus']}")
print(f" ▶ Intention : {resultat['intention']}")
