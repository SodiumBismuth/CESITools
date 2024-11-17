import streamlit as st
st.title("Postmortem")
"Étape 1 : Aller sur moodle et accédez à votre session"
"Étape 2 : Cliquez sur le bloc dont vous faites le postmortem"
"Étape 3 : Si ce n'est pas fait, dépliez tout les prosits de la page"
"Étape 4 : Appuyez sur ctrl+a puis sur ctrl+c"
"Étape 5 : Collez le texte dans le carré ci-dessous"
a = st.text_area("Insérez le texte de la page")
b = [[i[1], i[4:]] for i in a.split('\n') if i.startswith('[')]
st.dataframe(b)
f"Il y a {len(b)} AAV. Ajoutez {len(b)-12} lignes au postmortem pour tous les mettre."
