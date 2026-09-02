"""
Skapa minst fyra NumPy‑arrayer:
En 1D‑array med valfria heltal
En 2D‑array (3x3) med heltal
En sekvens med np.arange
En 2D‑array med slumpade heltal (np.random.randint)
Beräkna:
Summan av alla element i varje array
Summan per rad och per kolumn för de 2D‑arrayerna
Medelvärde för minst två av arrayerna
Filtrera:
Alla värden större än ett visst tal (t.ex. > 5 eller > 20)
Alla jämna tal i en av arrayerna
Alla värden inom ett intervall (t.ex. 10–30)
"""

import numpy as np

a = np.array([0,1,5,8,9,6,5,3])
print(a)
b = np.array([[5,6,9,0],[3,1,4,7]])
print(b)
c = np.arange(8).reshape(2,4)
print(c)
d = np.random.randint(0,10, size = (2,4))
print(d)

print(f"summan av a är: {np.sum(a)}")
print(f"summan av b är {np.sum(b)}")
print(f"summan av c är {np.sum(c)}")
print(f"summan av d är {np.sum(d)}")
print(f"radsumman av a är: {a.sum(axis=0)}")   # axis 0 blir radsumma pga 1d, det är första dimensionen, kan skrivas helt utan axis
print(f"kolumnsumman av b är: {b.sum(axis=0)}") # axis 0 blir kolumnsumma pga 2d, det är första dimensionen
print(f"radsumman av b är: {b.sum(axis=1)}")
print(f"kolumnsumman av c är: {c.sum(axis=0)}")
print(f"radsumman av c är: {c.sum(axis=1)}")
print (f"kolumnsumman av d är: {d.sum(axis=0)}")
print (f"radsumman av d är: {d.sum(axis=1)}")
print(f"medelvärdet för a är:{np.average(a)} ")
print(f"medelvärdet för d är:{np.average(d)}")
print(f"i a är dessa större än 5: {a[a > 5]}")
print(f"i b är dessa tal jämna: {b[b % 2 == 0]}")
print(f"i c är dessa tal mellan 2 och 5: {c[(c >= 2) & (c <= 5)]}")
"""
Kombinera:
Beräkna summan och medelvärdet av de filtrerade värdena
Räkna hur många värden som uppfyller varje villkor
(Extra) Filtrera rader i en 2D‑array baserat på rad-summa.
"""
print(np.sum(a[a > 5]))
print(np.average(a[a > 5]))
antal = np.sum(a > 5)                # antal true får man utan a[a > 5] det blir (a > 5)
print(antal)
print ((c[c.sum(axis=1) > 20]).sum())  # summerar först ihop raderna, plockar ut vilka som är över 20 i arrayen c.
                                       # printar sedan summan av den raden. istället för 4,5,6,7
