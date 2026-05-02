# -*- coding: utf-8 -*-
"""python3 gen.py  →  index.md  (200 ιστορία + 100 πολιτισμός/επιστήμη)"""
import os
import re

OUT = os.path.join(os.path.dirname(__file__), "index.md")
DATA = os.path.join(os.path.dirname(__file__), "data.txt")


def clip(s, max_w=100):
    w = s.split()
    return " ".join(w[:max_w]) if len(w) > max_w else s


def esc(s):
    return s.replace("|", "/")


def load_data():
    """Γραμμές: H|sk|ετικέτα|τίτλος|περιγραφή  ή  K|..."""
    hist, cult = [], []
    with open(DATA, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split("|", 4)
            if len(parts) < 5:
                continue
            kind, sk_s, lab, title, desc = parts[0].strip(), parts[1].strip(), parts[2].strip(), parts[3].strip(), parts[4].strip()
            sk = int(sk_s)
            row = (sk, lab, title, clip(desc, 100))
            if kind.upper() == "H":
                hist.append(row)
            else:
                cult.append(row)
    return hist, cult


def main():
    hist, cult = load_data()
    seen_h, uh = set(), []
    for sk, lab, t, d in sorted(hist, key=lambda x: x[0], reverse=True):
        k = (sk, t)
        if k in seen_h:
            continue
        seen_h.add(k)
        uh.append((sk, lab, t, d))
    seen_c, uc = set(), []
    for sk, lab, t, d in sorted(cult, key=lambda x: x[0], reverse=True):
        k = (sk, t)
        if k in seen_c:
            continue
        seen_c.add(k)
        uc.append((sk, lab, t, d))

    if len(uh) < 200:
        raise SystemExit(f"Χρειάζονται ≥200 ιστορικές γραμμές στο data.txt, βρέθηκαν {len(uh)}")
    if len(uc) < 100:
        raise SystemExit(f"Χρειάζονται ≥100 πολιτισμού στο data.txt, βρέθηκαν {len(uc)}")

    uh = uh[:200]
    uc = uc[:100]
    merged = [(sk, lab, t, d, "H") for sk, lab, t, d in uh] + [(sk, lab, t, d, "K") for sk, lab, t, d in uc]
    merged.sort(key=lambda x: (x[0], x[2]), reverse=True)

    if len(merged) != 300:
        raise SystemExit(f"Αναμενόταν 300 γραμμές, έχουμε {len(merged)}")

    lo, hi = min(x[0] for x in merged), max(x[0] for x in merged)
    # Παλαιότερο άκρο: βαθύς γεωλογικός χρόνος (π.χ. ~66 Ma)· ανώτερο όριο 1000 π.Χ. (sk -999)
    if hi > -999 or lo < -100_000_000:
        raise SystemExit(f"Έλεγχος εύρους απέτυχε: sk από {lo} έως {hi}")

    header = """---
Title: Προϊστορία
Description: Τριακόσια σημαντικά γεγονότα — από την αρχή της ανθρώπινης εξέλιξης έως το 1000 π.Χ. (ιστορία, επιστήμη, οικονομία, θρησκεία, τέχνες)
Author: Πέτρος
Date: 2026-05-02
Robots: noindex,nofollow
Template: index
---

|Ημερομηνία / Έτος|Τίτλος|Περιγραφή (έως 100 λέξεις)|
| ----- | ----- | ----- |
"""
    body = "".join(f"|{esc(lab)}|{esc(t)}|{esc(d)}|\n" for _, lab, t, d, _ in merged)
    open(OUT, "w", encoding="utf-8").write(header + body)
    print("Wrote 300 rows ->", OUT)


if __name__ == "__main__":
    main()
