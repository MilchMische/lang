import streamlit as st
import pandas as pd
import random
import time

# Funktion zum Laden der hochgeladenen Datei und zur Inspektion des Dateiinhalts
def load_data(uploaded_file):
    try:
        # Datei einlesen und nur die Spalten mit den relevanten Daten behalten
        data = pd.read_csv(uploaded_file, sep="\t", header=None, usecols=[1, 3], on_bad_lines="warn")
        
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

# Daten nach Upload speichern
if uploaded_file is not None:
    st.session_state['data'] = load_data(uploaded_file)

# Funktion zum Anzeigen eines zufälligen Satzes
def display_sentence():
    if 'data' in st.session_state and st.session_state['data'] is not None:
        data = st.session_state['data']
        # Zufälligen Index für den Satz auswählen
        random_index = random.randint(0, len(data) - 1)
        italian_sentence = data.iloc[random_index, 0]
        english_translation = data.iloc[random_index, 1]
        return italian_sentence, english_translation
    else:
        return None, None

# Fade-In & Fade-Out Animation für beide Sätze gleichzeitig
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

# Anzeige der Sätze mit dynamischem Update
sentence_block = st.empty()  # Ein Block für beide Sätze

if 'data' in st.session_state:
    if st.button("Datei neu einlesen"):
        st.session_state['start_display'] = True
    
    # Automatisches Wechseln der Sätze alle 6 Sekunden
    if 'start_display' not in st.session_state:
        st.session_state['start_display'] = True

    if st.session_state['start_display']:
        while True:
            italian_sentence, english_translation = display_sentence()
            if italian_sentence and english_translation:
                # Beide Sätze im selben Block anzeigen
                sentence_block.markdown(f"""
                <div class='fade'>
                    <h3>{italian_sentence}</h3>
                    <h3>{english_translation}</h3>
                </div>
                """, unsafe_allow_html=True)
                time.sleep(6)  # 6 Sekunden warten, bevor die Sätze wechseln
else:
    st.write("Lade eine Datei hoch, um zu beginnen.")
