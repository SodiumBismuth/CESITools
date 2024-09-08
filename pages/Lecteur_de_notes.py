import streamlit as st
import pdfplumber as pp
import pandas as pd

# Constantes
NOTE_EQUIV_NUM = {
    "A": 5,
    "C / A": 5,
    "D / A": 5,
    "B": 4,
    "C / B": 4,
    "D / B": 4,
    "C": 2,
    "D / C": 2,
    "D": 1,
    '': 1
}


# Fonction pour extraire les tableaux des pages PDF
def extraire_tables(pdf):
    tables = []
    for page in pdf.pages:
        table = page.extract_table()
        if table:
            tables.append(table)
    return tables


# Fonction pour traiter les données des tableaux
def traiter_donnees(tables):
    header = tables[0][0]
    data = []
    for table in tables:
        data.extend(table[1:])
    return pd.DataFrame(data, columns=header)


# Fonction pour calculer la note finale basée sur la moyenne
def calculer_note_finale(moyenne):
    if moyenne >= 4.6:
        return 'A'
    elif moyenne >= 3.6:
        return 'B'
    elif moyenne < 1.6:
        return 'D'
    else:
        return 'C'


# Affichage de l'application
st.title('Lecteur de notes')
dossier = st.file_uploader("Importer le dossier de synthèse", type="pdf", accept_multiple_files=False)

if dossier is not None:
    with pp.open(dossier) as pdf:
        tables = extraire_tables(pdf)

    df = traiter_donnees(tables)
    evaluations = []
    cur_axe = cur_ue = None

    for _, row in df.iterrows():
        if pd.isna(row[4]):
            cur_axe = row[0]  # Axe détecté
        elif pd.isna(row[3]):
            cur_ue = row[0]  # UE détectée
        else:
            # Enregistrement de l'évaluation
            evaluations.append([cur_axe, cur_ue, row[0], NOTE_EQUIV_NUM.get(row[2], 1), int(row[3])])

    # Conversion en DataFrame
    evaluations_df = pd.DataFrame(evaluations, columns=['axe', 'ue', 'ee', 'note', 'coef'])

    # Maintenir l'ordre d'apparition des axes et des UE
    evaluations_df['axe'] = pd.Categorical(evaluations_df['axe'], categories=evaluations_df['axe'].unique(),
                                           ordered=True)
    evaluations_df['ue'] = pd.Categorical(evaluations_df['ue'], categories=evaluations_df['ue'].unique(), ordered=True)

    # Groupement et affichage par axe en respectant l'ordre d'apparition
    for axe, group in evaluations_df.groupby('axe', sort=False):
        st.subheader(axe)
        ues = group['ue'].unique()
        ue_col = st.columns(len(ues))

        for idx, ue in enumerate(ues):
            with ue_col[idx]:
                ees = group[group['ue'] == ue]
                moyenne = round((ees['note'] * ees['coef']).sum() / ees['coef'].sum(), 2)
                note_finale = calculer_note_finale(moyenne)
                delta = round(moyenne - 3.6, 2)
                st.metric(ue, note_finale, delta=delta)

                if note_finale in "CD":
                    st.markdown('##### E.E. à rattraper / à faire :')
                    ees_a_rattraper = ees[ees['note'] < 3]
                    for _, ee in ees_a_rattraper.iterrows():
                        st.write(ee['ee'])
