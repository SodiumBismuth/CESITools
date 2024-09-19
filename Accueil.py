import streamlit as st

st.title('CESITools')
st.header("L'outil pratique pour votre année !")
st.subheader('Applications disponibles')
notes,prosit = st.columns(2)

with notes:
    st.header('Lecteur de notes')
    st.image('res/notes.png',width=100)
    st.write("Le lecteur de notes permet facilement d'étudier son dossier de synthèse ainsi que de savoir quelles "
             "épreuves doivent être rattrapées.")
    st.page_link('pages/Lecteur_de_notes.py',label='Y aller',icon=':material/arrow_forward:')

with prosit:
    st.header('Éditeur de prosit')
    st.image('res/editeur.png',width=100)
    st.markdown("L'éditeur de prosit permet de créer de A à Z un PDF prêt à être envoyé du prosit aller en cours. **Il supporte en plus le markdown !**")
    st.page_link('pages/Éditeur_de_prosit.py',label='Y aller',icon=':material/arrow_forward:')