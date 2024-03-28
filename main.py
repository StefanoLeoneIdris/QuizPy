import os
import random
from flask import Flask, render_template, request

main = Flask(__name__)

#consistenza dati tramite file .txt
def get_best_score():
    if not os.path.exists('best_score.txt'):
        with open('best_score.txt', 'w') as file:
            file.write('0')
    with open('best_score.txt', 'r') as file:
        return int(file.read())

#consistenza dati tramite file .txt. Aggiornamento best score
def update_best_score(new_score):
    current_best_score = get_best_score()
    if new_score > current_best_score:
        with open('best_score.txt', 'w') as file:
            file.write(str(new_score))
        return new_score
    return current_best_score

#estrazione di solo 10 domande casuali; shuffle risposte
def get_random_quiz_questions():
  R_quiz = random.sample(quiz, 10)
  for question in quiz:
    random.shuffle(question["choices"])
  return R_quiz

#render_template homepage
@main.route('/')
def index():
  R_quiz = get_random_quiz_questions()
  return render_template('index.html', quiz=R_quiz, best_score=get_best_score())

#render_template result page
@main.route('/submit', methods=['POST'])
def submit():
    score = 0
    for q in quiz:
        user_answer = request.form.get(q['question'])
        if user_answer == q['answer']:
            score += 1
    new_best_score = update_best_score(score)
    return render_template('result.html', score=score, quiz=quiz, get_best_score=get_best_score, new_best_score=new_best_score)

#array domande con shuffle
quiz = [
    {
        "question": "Che cos'è la visione computerizzata?",
        "choices": ["Un campo dell'informatica che si occupa dell'analisi e interpretazione di immagini e video", 
                    "Un metodo per la gestione dei database", 
                    "Una tecnologia per la comunicazione wireless", 
                    "Una strategia per lo sviluppo di algoritmi di ordinamento"],
        "answer": "Un campo dell'informatica che si occupa dell'analisi e interpretazione di immagini e video"
    },
    {
        "question": "Quali sono alcuni esempi di applicazioni pratiche della visione computerizzata?",
        "choices": ["Riconoscimento facciale", "Gestione delle risorse umane", "Sviluppo di siti web", "Pianificazione finanziaria"],
        "answer": "Riconoscimento facciale"
    },
    {
        "question": "Come vengono utilizzati gli algoritmi di visione computerizzata nell'accessibilità audiovisiva?",
        "choices": ["Per descrivere il contenuto visivo ai non vedenti", 
                    "Per migliorare la qualità audio dei video", 
                    "Per creare effetti speciali nei film", 
                    "Per identificare errori di pronuncia nella trascrizione di audio"],
        "answer": "Per descrivere il contenuto visivo ai non vedenti"
    },
    {
        "question": "Qual è il ruolo dell'intelligenza artificiale nell'accessibilità audiovisiva?",
        "choices": ["Utilizzare algoritmi di visione computerizzata per descrivere immagini e video", 
                    "Creare playlist musicali personalizzate", 
                    "Sviluppare nuove tecnologie di illuminazione per il cinema", 
                    "Registrare podcast"],
        "answer": "Utilizzare algoritmi di visione computerizzata per descrivere immagini e video"
    },
    {
        "question": "Quali sono alcuni esempi di modelli di intelligenza artificiale utilizzati nella visione computerizzata?",
        "choices": ["Reti neurali convoluzionali (CNN)", 
                    "Algoritmi di ordinamento", 
                    "Metodi di ricerca testuale", 
                    "Tecniche di compressione dei dati"],
        "answer": "Reti neurali convoluzionali (CNN)"
    },
    {
        "question": "Come vengono addestrati i modelli di visione computerizzata?",
        "choices": ["Con un ampio dataset di immagini etichettate", 
                    "Con la memorizzazione di schemi di progettazione di circuiti elettronici", 
                    "Con l'analisi delle previsioni meteo", 
                    "Con l'utilizzo di codice sorgente open source"],
        "answer": "Con un ampio dataset di immagini etichettate"
    },
    {
        "question": "Qual è il vantaggio dell'utilizzo di reti neurali convoluzionali (CNN) nella visione computerizzata?",
        "choices": ["Possono apprendere caratteristiche rilevanti dalle immagini senza la necessità di un'ingegneria manuale delle feature", 
                    "Sono in grado di generare codice sorgente automaticamente", 
                    "Richiedono una quantità minima di dati di addestramento", 
                    "Possono essere utilizzate solo per la classificazione di testo"],
        "answer": "Possono apprendere caratteristiche rilevanti dalle immagini senza la necessità di un'ingegneria manuale delle feature"
    },
    {
        "question": "Quali sono le sfide comuni nella visione computerizzata?",
        "choices": ["Variabilità delle condizioni di illuminazione", 
                    "Facilità di acquisizione dei dati", 
                    "Accessibilità dei dispositivi hardware", 
                    "Disponibilità di connessione Internet ad alta velocità"],
        "answer": "Variabilità delle condizioni di illuminazione"
    },
    {
        "question": "In che modo la visione computerizzata può essere utilizzata per migliorare la sicurezza?",
        "choices": ["Rilevando attività sospette in immagini o video di sorveglianza", 
                    "Facilitando la gestione dei social media", 
                    "Monitorando il traffico online", 
                    "Creando filtri di spam per l'email"],
        "answer": "Rilevando attività sospette in immagini o video di sorveglianza"
    },
    {
        "question": "Quali sono alcune applicazioni innovative della visione computerizzata in ambito medico?",
        "choices": ["Diagnosi assistita da computer per immagini mediche", 
                    "Gestione delle prescrizioni online", 
                    "Prenotazioni di appuntamenti medici tramite app", 
                    "Sviluppo di videogiochi educativi per medici"],
        "answer": "Diagnosi assistita da computer per immagini mediche"
    },
    {
        "question": "Che cos'è il clustering nell'intelligenza artificiale?",
        "choices": ["Un metodo per suddividere un insieme di dati in gruppi omogenei", 
                    "Un algoritmo per creare modelli di regressione lineare", 
                    "Una tecnica per addestrare reti neurali profonde", 
                    "Un approccio per eseguire l'analisi delle componenti principali"],
        "answer": "Un metodo per suddividere un insieme di dati in gruppi omogenei"
    },
    {
        "question": "Qual è l'obiettivo principale del clustering?",
        "choices": ["Raggruppare i dati in modo che gli elementi all'interno di ogni gruppo siano simili tra loro", 
                    "Creare una previsione precisa di un risultato futuro", 
                    "Valutare le prestazioni di un modello di machine learning", 
                    "Calcolare le derivate di una funzione"],
        "answer": "Raggruppare i dati in modo che gli elementi all'interno di ogni gruppo siano simili tra loro"
    },
    {
        "question": "Quale algoritmo di clustering è noto per dividere i dati in cluster di forma sferica?",
        "choices": ["K-Means", "DBSCAN", "Hierarchical Clustering", "Affinity Propagation"],
        "answer": "K-Means"
    },
    {
        "question": "Qual è l'obiettivo principale dell'algoritmo DBSCAN?",
        "choices": ["Identificare cluster di forma arbitraria nel dataset", 
                    "Dividere i dati in cluster di forma sferica", 
                    "Creare una rete neurale profonda", 
                    "Generare predizioni accurate su dati non visti"],
        "answer": "Identificare cluster di forma arbitraria nel dataset"
    },
    {
        "question": "Come viene misurata la similarità tra punti nei metodi di clustering?",
        "choices": ["Utilizzando metriche come la distanza euclidea o la similarità del coseno", 
                    "Controllando il tempo di esecuzione dell'algoritmo", 
                    "Confrontando il numero di cluster generati", 
                    "Analizzando la dimensione dei dati in input"],
        "answer": "Utilizzando metriche come la distanza euclidea o la similarità del coseno"
    }
      
  ]

if __name__ == '__main__':
    main.run(debug=True)
