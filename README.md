# 🎮 School Project 2026 - Progetto Python

## 📌 Descrizione
Questo progetto è un'applicazione sviluppata in Python che utilizza la libreria **Pygame** per creare un ambiente grafico interattivo.  
Utilizza anche i moduli standard **math**, **time** e **random** per gestire rispettivamente calcoli matematici, controllo del tempo ed elementi casuali.

Il progetto è molto semplice. E' stato creato nel corso di una competizione amichevole di due ore.

---

## 🚀 Funzionalità
- Grafica 2D con Pygame
- Loop di gioco con gestione FPS
- Logica matematica
- Eventi casuali con `random`
- Controllo del tempo con `time`

---

## 🧰 Requisiti

- Python 3.8+
- Pygame

### Installazione
```bash
pip install pygame
```

---

## ▶️ Avvio del progetto

```bash
python main.py
```

---

## 🎮 Controlli e regole

- WASD → Movimento giocatore A
- IJKL → Movimento giocatore B
- Per uscire dal gioco premere la X

- Il gioco prevede che uno dei giocatori insegua l'altro. Se lo prende, vince, altrimenti, vince l'altro se resiste per 30 secondi (time in alto a sinistra)
- I muri sono generati casualmente e impediscono il movimento

---

## 📁 Struttura del progetto

```text
school-project-2026-3/
├── main.py             # Il gioco principale
├── main1.py            # Currently being developed
├── .venv/
│   └── libraries       # If you choose to download them with the project
├── images/
│   └── various images
└── sounds/
    └── various sounds
```
---

## 📦 Librerie utilizzate

- pygame → gestione grafica, eventi e loop di gioco  
- math → operazioni matematiche  
- time → gestione del tempo e timing  
- random → generazione di eventi casuali  

---

## 💡 Note

- Se volete installare le librerie in un ambiente vosto, potete farlo, altrimenti se scaricate anche il  `.venv/` le  liberie sono già lì pronte
- `main.py` è il gioco principale, `main1.py` è un'altra versione che vorremmo sviluppare in fututo, per aumentare la qualità del gioco, già questionabile al momento. Per ora non funziona bene.
- Se il giocatore prova ad andare addosso ad un muro e lateralmente allo stesso tempo, rimarra fermò. Questo bug è noto e verrà fixato un giorno (forse).

---

## 👨‍💻 Autore
Progetto sviluppato in Python come esercizio con Pygame durante una competizione amichevole. Due persone hanno sviluppato questo progetto in due ore.
