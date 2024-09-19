import streamlit as st
from generate_pdf import generate_pdf
from io import BytesIO

def main():
    st.title("Demande de Congé Professionnel")
    st.markdown("Remplissez le formulaire ci-dessous pour générer une demande de congé professionnel.")

    with st.form(key='conge_form'):
        # Section Informations Personnelles
        st.subheader("Informations Personnelles")
        col1, col2 = st.columns([1, 1])
        
        with col1:
            nom = st.text_input("Nom", max_chars=50)
        
        with col2:
            prenom = st.text_input("Prénom", max_chars=50)
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            service = st.text_input("Service", max_chars=50)
        
        with col2:
            fonction = st.text_input("Fonction", max_chars=50)
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            adresse = st.text_input("Adresse du lieu de congé", max_chars=100)
        
        with col2:
            telephone = st.text_input("Téléphone", max_chars=15)
        
        st.write("")  # Adding some vertical space
        
        # Section Détails du Congé
        st.subheader("Détails du Congé")
        col1, col2 = st.columns([1, 1])
        
        with col1:
            reliquat = st.number_input("Reliquat restant sur la situation", min_value=0, step=1, format="%d")
        
        with col2:
            droit_annuel = st.number_input("Droit de l’année en cours", min_value=0, step=1, format="%d")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            total_droits = st.number_input("Total des droits", min_value=0, step=1, format="%d")
        
        with col2:
            motif = st.text_input("Motif du congé", max_chars=100)
        
        st.write("")  # Adding some vertical space
        
        # Date Inputs
        st.subheader("Période du Congé")
        col1, col2 = st.columns([1, 1])
        
        with col1:
            date_depart = st.date_input("Date de départ")
        
        with col2:
            date_reprise = st.date_input("Date de reprise")
        
        st.write("")  # Adding some vertical space
        
        # Durée Totale
        duree_totale = st.number_input("Durée totale prise (jours)", min_value=0, step=1, format="%d")
        
        st.write("")  # Adding some vertical space
        
        # Submit button inside the form
        submit_button = st.form_submit_button("Générer PDF")

    # Place st.download_button() outside the form
    if submit_button:
        data = {
            'nom': nom,
            'prenom': prenom,
            'service': service,
            'fonction': fonction,
            'adresse': adresse,
            'telephone': telephone,
            'reliquat': reliquat,
            'droit_annuel': droit_annuel,
            'total_droits': total_droits,
            'motif': motif,
            'date_depart': date_depart.strftime('%d/%m/%Y'),
            'date_reprise': date_reprise.strftime('%d/%m/%Y'),
            'duree_totale': duree_totale
        }

        # Generate PDF and save to a BytesIO object
        pdf_buffer = BytesIO()
        generate_pdf(data, pdf_buffer)  # Provide the BytesIO stream as the output

        # Move st.download_button() outside the form
        st.download_button(
            label="Télécharger le PDF",
            data=pdf_buffer.getvalue(),
            file_name="demande_conge.pdf",
            mime="application/pdf"
        )

if __name__ == "__main__":
    main()
