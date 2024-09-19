import streamlit as st
from datetime import datetime
from io import BytesIO
from generate_reparation import generate_pdf

def main():
    st.title("Formulaire de Demande de Réparation")
    st.markdown("Remplissez le formulaire ci-dessous pour générer une demande de réparation.")

    # Initialize session state for PDR Concernés
    if 'pieces' not in st.session_state:
        st.session_state.pieces = []

    with st.form(key='reparation_form'):
        # Informations de base
        st.subheader("Informations Demande")
        nom = st.text_input("Nom", "", max_chars=50)
        date = st.date_input("Date", datetime.today())
        date_livraison = st.date_input("Date de livraison chez client et mise en service", datetime.today())
        client = st.text_input("Client", "", max_chars=50)

        # PDR Concernés
        st.subheader("PDR Concernés")
        piece_reference = st.text_input("Référence Pièce", "", max_chars=50)
        designation = st.text_input("Désignation", "", max_chars=50)
        quantity = st.number_input("QTE", min_value=0, step=1)
        n_serie = st.text_input("N° Série", "", max_chars=50)

        add_piece = st.form_submit_button("Ajouter la ligne")

        if add_piece:
            st.session_state.pieces.append((piece_reference, designation, quantity, n_serie))

        # Display the table data
        st.write("### PDR Concernés ajoutés")
        for i, (ref, des, qty, serie) in enumerate(st.session_state.pieces):
            st.write(f"Référence: {ref}, Désignation: {des}, QTE: {qty}, N° Série: {serie}")

        # Machine concernée and other info
        st.subheader("Machine Concernée")
        machine_concernee = st.text_area("Machine concernée", "", max_chars=200)
        etat_machine = st.text_input("Etat machine", "", max_chars=50)
        type_machine = st.text_input("Type de machine", "", max_chars=50)
        lieu = st.text_input("Lieu", "", max_chars=50)

        # Signatures
        st.subheader("Signatures")
        signature_demandeur = st.text_input("Signature Demandeur", "", max_chars=50)

        # Bouton pour soumettre le formulaire
        submit_button = st.form_submit_button("Générer PDF")

    if submit_button:
        data = {
            'date': date.strftime('%d/%m/%Y'),
            'nom': nom,
            'date_livraison': date_livraison.strftime('%d/%m/%Y'),
            'client': client,
            'machine_concernee': machine_concernee,
            'alternative_machines': machine_concernee,
            'etat_machine': etat_machine,
            'type_machine': type_machine,
            'lieu': lieu,
            'signature_demandeur': signature_demandeur
        }
        
        pieces = [(ref, des, str(qty), serie) for ref, des, qty, serie in st.session_state.pieces]

        pdf_buffer = BytesIO()
        generate_pdf(data, pieces, pdf_buffer)
        pdf_buffer.seek(0)
        
        st.download_button(label="Télécharger PDF", data=pdf_buffer, file_name="demande_reparation.pdf", mime="application/pdf")

if __name__ == '__main__':
    main()
