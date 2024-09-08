import streamlit as st

st.title('CESITools')
st.header("L'outil pratique pour votre année !")
st.subheader('Applications disponibles')
notes,prosit = st.columns(2)

with notes:
    st.header('Lecteur de notes')
    #st.image()
    st.write("Le lecteur de notes permet facilement d'étudier son dossier de synthèse ainsi que de savoir quelles "
             "épreuves doivent être rattrapées.")
    st.page_link('pages/Lecteur_de_notes.py',label='Y aller')

with prosit:
    st.header('Éditeur de prosit')
    #st.image()
    st.write("L'éditeur de prosit permet de créer de A à Z un PDF prêt à être envoyé du prosit aller en cours.")
    st.page_link('pages/Éditeur_de_prosit.py',label='Y aller')
