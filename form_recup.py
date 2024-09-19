# form.py

import streamlit as st
from datetime import datetime
from io import BytesIO
from generate_recup import generate_pdf

def main():
    st.title("Formulaire de Demande de Pièces")
    st.markdown("Remplissez le formulaire ci-dessous pour générer une demande de récupération de pièces.")

    # Initialize session state for pieces
    if 'pieces' not in st.session_state:
        st.session_state.pieces = []

    with st.form(key='demande_form'):
        # Informations de base
        st.subheader("Informations Demande")
        nom_demandeur = st.text_input("Nom demandeur", "service technique SANY", max_chars=50)
        date_demande = st.date_input("Date demande", datetime.today())
        type_machine = st.text_input("Type de machine", "SW405K", max_chars=50)
        serie_stock = st.text_input("N° de série machine stock", "SW4054C00368", max_chars=50)
        fiche_machine = st.text_input("N° Fiche machine", "6102", max_chars=50)

        # Pour client
        st.subheader("Pour Client")
        pour_client = st.text_input("Pour client", "HAMRI", max_chars=50)
        etat_machine = st.text_input("Etat machine", "En arrêt", max_chars=50)
        type_machine_client = st.text_input("Type de machine client", "SW405K", max_chars=50)
        serie_stock_client = st.text_input("N° de série machine stock client", "SW4054C00378", max_chars=50)
        fiche_machine_client = st.text_input("N° Fiche machine client", "6103", max_chars=50)

        # Signatures
        st.subheader("Signatures")
        visa_demandeur = st.text_input("Nom et Visa Demandeur", "LACHKAR AHMED SALIM")

        # Bouton pour soumettre le formulaire
        submit_button = st.form_submit_button("Générer PDF")

    st.subheader("Tableau des Pièces")
    piece_reference = st.text_input("Référence Pièce")
    designation = st.text_input("Désignation")
    quantity = st.number_input("QTE", min_value=0, step=1)

    if st.button("Ajouter la ligne"):
        st.session_state.pieces.append((piece_reference, designation, quantity))

    # Display the table data
    st.write("### Pièces ajoutées")
    for i, (ref, des, qty) in enumerate(st.session_state.pieces):
        st.write(f"Référence: {ref}, Désignation: {des}, QTE: {qty}")

    if submit_button:
        data = {
            'nom_demandeur': nom_demandeur,
            'date_demande': date_demande.strftime('%d/%m/%Y'),
            'type_machine': type_machine,
            'serie_stock': serie_stock,
            'fiche_machine': fiche_machine,
            'pour_client': pour_client,
            'etat_machine': etat_machine,
            'type_machine_client': type_machine_client,
            'serie_stock_client': serie_stock_client,
            'fiche_machine_client': fiche_machine_client,
            'visa_demandeur': visa_demandeur
        }

        pieces = st.session_state.pieces

        # Generate PDF
        pdf_buffer = BytesIO()
        generate_pdf(data, pieces, pdf_buffer)

        # Download button for the PDF
        st.download_button(
            label="Télécharger le PDF",
            data=pdf_buffer.getvalue(),
            file_name="demande_pieces.pdf",
            mime="application/pdf"
        )

if __name__ == "__main__":
    main()
