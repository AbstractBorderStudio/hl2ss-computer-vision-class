---
documentclass: article
colorlinks: true
toc: true

header-includes:
 - \usepackage{fancyhdr}
 - \pagestyle{fancy}
 - \rhead{\emph{ML for Vision \& Multimedia}}
 - \usepackage{tcolorbox}
 - \newtcolorbox{annotation}{colback=red!5!white, colframe=red!75!black}
 - \renewenvironment{quote}{\begin{annotation}}{\end{annotation}}
 - \usepackage{abstract}
 - \renewcommand{\abstractname}{About this document}
 - \usepackage{wrapfig}
 - \usepackage{subfig}
 - \setcounter{MaxMatrixCols}{20}
title: Riconoscimento e tracciamento di strumenti medicali mediante l'uso di Microsoft Hololens 2
subtitle: |
  | Docente:
  | Montrucchio Bartolomeo, DAUIN (bartolomeo.montrucchio@polito.it)
  | Referenti:
  | Ulrich Luca, 3DLab (luca.ulrich@polito.it)
  | Marullo Giorgia, 3DLab (giorgia.marullo@polito.it)
author: |
  | Autori:
  | Bologna Daniel
  | Plumari Martina
  | Pasini Ilaria
date: \today
abstract: |
  | Questo progetto propone l'implementazione di una soluzione avanzata per il riconoscimento e il tracciamento di strumenti medici utilizzando Microsoft HoloLens 2, un dispositivo di realtà mista. 
  |
  | L'obiettivo principale è migliorare l'efficienza e la sicurezza delle procedure mediche, consentendo ai professionisti sanitari di riconoscere e monitorare gli strumenti medici in tempo reale durante interventi chirurgici e procedure diagnostiche.
---

\Large
\pagebreak

# Introduzione

Questo progetto propone l'implementazione di una soluzione avanzata per il riconoscimento e il tracciamento di strumenti medici utilizzando [Microsoft HoloLens 2](https://www.microsoft.com/it-it/hololens), un dispositivo di realtà mista. L'obiettivo principale è migliorare l'efficienza e la sicurezza delle procedure mediche, consentendo ai professionisti sanitari di riconoscere e monitorare gli strumenti medici in tempo reale durante interventi chirurgici e procedure diagnostiche.

Il sistema sfrutta la potenza della visione artificiale e dell'apprendimento automatico per identificare automaticamente gli strumenti medici, etichettarli e tenere traccia della loro posizione all'interno del campo visivo del chirurgo o dell'operatore. Il tutto viene visualizzato in sovraimpressione sull'ambiente reale attraverso le HoloLens 2, consentendo ai professionisti di avere una visione chiara e dettagliata dei dispositivi medici in uso.

Questo approccio innovativo può ridurre il rischio di errori umani, aumentare l'efficienza operativa e migliorare la comunicazione all'interno del team medico. Il progetto potrebbe avere un impatto significativo sulla qualità delle cure mediche e aprire la strada a nuove applicazioni di realtà mista nella pratica medica.

# Overview del progetto

Ci si propone di sviluppare un applicativo che sfrutti la potenza della realtà mista fornito dal sistema Hololens 2 di Microsoft. L'applicativo sarà sviluppato mediante l'utilizzo del software Unity 3D e della libreria [MRTK 3](https://learn.microsoft.com/it-it/windows/mixed-reality/mrtk-unity/mrtk3-overview/), che permette di accedere alla potenzialità del visore.

Inoltre, sarà necessario poter accedere ai flussi video provenienti dai **sensori** del visore, per applicare degli algoritmi di **computer vision**. Per questo motivo abbiamo selezionato, sotto consiglio 3 possibili librerie ufficiali per gestire questo aspetto del progetto:

- [HoloLens2ForCV](https://github.com/microsoft/HoloLens2ForCV)
  - (questo dovrebbe essere il migliore da integrare in unity) 
  - da buildare direttamente su Hololens, non serve Unity, 
    - permette di accedere ai flussi video, 
    - vederli direttamente su hololens 2 
    - registrare i flussi per processamento offline tramite degli script python
- [hl2ss](https://github.com/jdibenes/hl2ss)
  - permette di accedere ai flussi video in tempo reale mediante script python
- [HoloLens2-ResearchMode-Unity](https://github.com/petergu684/HoloLens2-ResearchMode-Unity)
  - simile al primo progetto ma implementato in Unity;

## Come usare il visore (da rimuovere)

- **Password hololens**: 02 01 98

>Quando ci si connette al portale su browser bisogna inserire l'ip del Hololens sul browser

- **Indirizzo ip hololens**: 169.254.58.146

\begin{figure}[h]
    \centering
    \includegraphics[width=8cm]{imgs/2023-10-14-15-04-31.png}
\end{figure}

>Quando si accede la prima volta, sul browser viene segnalato che la pagina potrebbe essere malevola. Andare avanti.
>
>Spunterà un popup che richiede uno username e una password per continuare:

- **user**: hololens
- **pass**: hololens

In questo modo si può accedere al **Windows Portal Device**. In questa interfaccia si possono

- registrare dei video direttamente dalla camera principale.
- installare/disinstallare/aggiornare applicazioni sull'hololen
- accedere alla **reserach mode** (di default tutti e due gli hololens hanno questa modalità attiva)

\begin{figure}[h]
    \centering
    \includegraphics[width=10cm]{imgs/image-1.png}
\end{figure}

Per prendere l'immagine precedente abbiamo attivato un'applicazione all'intrno del visore che facesse vedere i flussi video. Poi dal **Windows Device Portal** abbiamo avviato la cattura, escludendo il segnale video **VP** (video frontale a colori normale).


## Passaggi di sviluppo

1. **Visualizzare i flussi video dell'Hololens** (potrebbero essercene più di 4, il consiglio è di visualizzarli tutti per semplicità, così sapete poi quale è più comodo per voi)
   - Per farlo, conviene accedere al research mode Hololens
   - Visualizzare i pannelli contenenti i flussi video su Unity
   - Visualizzare i pannelli contenenti i flussi video su Hololens
2. Effettuare la **blob detection** (riconoscimento sferette)
   - Potete usare i flussi video che preferite, purché il risultato sia ottenere le <u>**coordinate in 3D**</u>
   - Se utilizzate flussi video provenienti da camere diverse, ricordate che occorre prima allinearli
   - E' possibile ottenere le coordinate in 3D utilizzando solo la camera AHAT (Articulated Hand Tracking)
   - La blob detection va implementata sull'Hololens (non basta la webcam, serve la profondità!)
   - Sovrapporre il modello 3D virtuale delle sferette all'oggetto reale
3. **Analisi accuratezza**
   - Calcolare la distanza tra le sferette virtuali e confrontare con la distanza tra le sferette reali.
   - Calcolare la distanza tra le sferette e la camera (tutto virtuale) e la distanza tra le sferette e la camera (tutto reale)
4. **Calcolo punta del tastatore a partire dai blob identificati** e confronto con le misure reali
   - By design: calcolare la posizione del tastatore a partire dalla posizione dei centri delle sferette
   - Pivoting: calcolare la posizione della punta dello strumento (pivot) come centro di sfere ai minimi quadrati. I punti che consentono di trovare le sfere ai minimi quadrati si ottengono mediante rilevazioni successive della posizione dei centri delle sferette mantenendo fissa la punta

# Visualizzazione dei flussi Hololens2

Durante il nostro percorso abbiamo preso in considerazione le seguenti librerie:

- [HoloLens2ForCV](https://github.com/microsoft/HoloLens2ForCV)
  - (questo dovrebbe essere il migliore da integrare in unity) 
  - da buildare direttamente su Hololens, non serve Unity, 
    - permette di accedere ai flussi video, 
    - vederli direttamente su hololens 2 
    - registrare i flussi per processamento offline tramite degli script python
- [hl2ss](https://github.com/jdibenes/hl2ss)
  - permette di accedere ai flussi video in tempo reale mediante script python

## Metodo 1

Nel primo caso abbiamo è stato presa in considerazione la possibilità di usare la libreria [HoloLens2ForCV](https://github.com/microsoft/HoloLens2ForCV).

Questa permette di 

- avviare un'applicazione all'interno dell'hololens2 che registra un insieme di dati
- scaricare offline i dati per successive elaborazioni

Il problema di questa libreria è che non presenta in modo evidente metodi per ottenere i flussi video in real time

## Metodo 2

Tramite [hl2ss](https://github.com/jdibenes/hl2ss), abbiamo 

- caricato un'applicativo all'interno dell'hololnes2 che apre un server e invia gli stream dei sensori.
- mediante uno script python abbiamo potuto connetterci a tale server per ottenere i dati in real time

# Blob detection

1. immagine in grayscale
2. applico kernel di smoting per ridurre il noise
3. eseguo una sogliatura per isolare solo gli elementi con una luminosità superiore alla soglia
4. applico un algoritmo di edge detection
5. 