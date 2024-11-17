import streamlit as st
from streamlit_tags import st_tags
from markdown_pdf import MarkdownPdf
from markdown_pdf import Section

st.title('Éditeur de prosit')

st.info("Il est possible d'utiliser le markdown ! https://www.markdownguide.org/cheat-sheet/")


prosit_steps = [
    "Mots Clés",
    "Contexte",
    "Problématique",
    "Contraintes",
    "Généralisation",
    "Livrable",
    "Pistes de solution",
    "Plan D'action"
]
titre = st.text_input("Titre du prosit")
a, b, c, d = st.columns(4)
secretaire = a.text_input("Nom du secrétaire")
scribe = b.text_input("Nom du scribe")
animateur = c.text_input("Nom de l'animateur")
gestionnaire = d.text_input("Nom du gestionnaire")

kw, ctx, pb, ct, gn, lv, ps, pa = st.tabs(prosit_steps)

with kw:
    keywords = st_tags(label="Entrez vos mots clés ici", text="Appuyez sur entrée pour ajouter un nouveau mot")

with ctx:
    context = st.text_area("Entrez votre/vos contexte(s) ici", height=250)

with pb:
    problematic = st.text_input("Entrez la problématique")

with ct:
    constraints = st.text_area("Insérez vos contraintes ici", height=250)

with gn:
    generalization = st_tags(label="Entrez vos mots de généralisation ici",
                             text="Appuyez sur entrée pour ajouter un nouveau mot")

with lv:
    deliverable = st.text_area("Insérez ce que le livrable devra contenir ici", height=250)

with ps:
    solution = st.text_area("Insérez les pistes de solutions ici", height=250)

with pa:
    action_plan = st.text_area("Insérez votre plan d'action ici", height=250)


# Fonction pour générer le PDF
def generate_pdf():
    global titre
    if titre is None or titre == "":
        titre = "untitled"
    # mise en forme des listes
    f_keywords = " - " + "\n - ".join(keywords)
    f_generalization = " - " + "\n - ".join(generalization)
    # Créer un contenu en Markdown avec les entrées utilisateur
    with open("template.txt", 'r',encoding="utf-8") as f:
        md_content = f.read().format(
            titre,
            secretaire,
            scribe,
            animateur,
            gestionnaire,
            f_keywords,
            context,
            problematic,
            constraints,
            f_generalization,
            deliverable,
            solution,
            action_plan
        )

    # Convertir le markdown en PDF

    pdf = MarkdownPdf(toc_level=1)
    pdf.add_section(Section(md_content), user_css="body {font-family:\"Arial\"}")
    pdf.writer.close()
    return pdf.out_file


if st.button("Generate PDF"):
    # Générer le PDF
    pdf_buffer = generate_pdf()

    print(pdf_buffer.read())

    # Convertir le buffer en fichier téléchargeable
    st.download_button(
        label="Download PDF",
        data=pdf_buffer,
        file_name=f"{titre}.pdf",
        mime="application/pdf"
    )
