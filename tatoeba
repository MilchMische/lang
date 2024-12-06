import streamlit as st
import pandas as pd
import random
import time

# Funktion zum Laden der hochgeladenen Datei und zur Inspektion des Dateiinhalts
def load_data(uploaded_file):
    try:
        # Datei einlesen und nur die Spalten mit den relevanten Daten behalten
        data = pd.read_csv(uploaded_file, sep="\t", header=None, usecols=[1, 3], on_bad_lines="skip")
        
        # Überprüfen, ob mindestens 2 Spalten vorhanden sind
        if data.shape[1] < 2:
            st.error(f"Die hochgeladene Datei enthält {data.shape[1]} Spalten. Erwartet werden mindestens 2 Spalten.")
            return None
        return data
    except pd.errors.ParserError as e:
        st.error(f"Fehler beim Laden der Daten: {e}")
        return None

# Streamlit app layout
st.title("Tatoeba Satzanzeige mit Fade-Effekt")

# Datei hochladen
uploaded_file = st.file_uploader("Lade eine TSV-Datei hoch", type=["tsv"])

# Wenn die Datei hochgeladen wurde, Daten laden und Sätze anzeigen
if uploaded_file is not None:
    data = load_data(uploaded_file)

    if data is not None:
        # Fade-In & Fade-Out Animation für den italienischen Satz und die Übersetzung
        st.markdown("""
        <style>
        .fade {
            animation: fadeInOut 6s;
        }
        @keyframes fadeInOut {
            0% { opacity: 0; }
            10% { opacity: 1; }
            90% { opacity: 1; }
            100% { opacity: 0; }
        }
        </style>
        """, unsafe_allow_html=True)

        # Wiederholter Wechsel der Sätze
        while True:
            # Zufälligen Index für den Satz auswählen
            random_index = random.randint(0, len(data) - 1)

            italian_sentence = data.iloc[random_index, 0]
            english_translation = data.iloc[random_index, 1]

            # Block für den italienischen Satz
            italian_block = st.empty()
            italian_block.markdown(f"<h3 class='fade'>{italian_sentence}</h3>", unsafe_allow_html=True)
            time.sleep(3)  # 3 Sekunden warten

            # Block für die englische Übersetzung
            english_block = st.empty()
            english_block.markdown(f"<h3 class='fade'>{english_translation}</h3>", unsafe_allow_html=True)
            time.sleep(3)  # 3 Sekunden warten

            # Lösche die Inhalte der vorherigen Sätze
            italian_block.empty()
            english_block.empty()
