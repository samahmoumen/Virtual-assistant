import streamlit as st
from generate_stage import generate_pdf
from io import BytesIO
from datetime import datetime


MONTHS_FR = {
    'January': 'Janvier', 'February': 'Février', 'March': 'Mars', 'April': 'Avril',
    'May': 'Mai', 'June': 'Juin', 'July': 'Juillet', 'August': 'Août',
    'September': 'Septembre', 'October': 'Octobre', 'November': 'Novembre',
    'December': 'Décembre'
}

def format_date_to_french(date_str):
    """Convert a date string in the format 'YYYY-MM-DD' to French."""
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    month = date_obj.strftime('%B')  # Get month name in English
    french_month = MONTHS_FR.get(month, month)  # Convert to French
    return date_obj.strftime(f'%d {french_month} %Y')  # Format the date

def main():
    
    st.title("Attestation de Stage")

    with st.form(key='attestation_form'):
        col1, col2 = st.columns(2)
        
        with col1:
            nom = st.text_input("Nom")
            prenom = st.text_input("Prénom")
            stage_intitule = st.text_input("Intitulé du Stage")
        
        with col2:
            genre = st.selectbox(
                "Choisissez le genre du stagiaire :",
                ["Monsieur", "Madame", "Mademoiselle"]
            )
            
            typeStage = st.selectbox(
                "Choisissez le type de stage :",
                ["stage d'initiation", "stage technique", "stage de fin d'etude"]
            )
            date_debut = st.date_input("Date de début")
            date_fin = st.date_input("Date de fin")
            service = st.text_input("Service")
            responsable_nom = st.text_input("Nom et Prénom du Responsable")
            responsable_titre = st.text_input("Titre du Responsable")

        st.subheader("Date de l'attestation")
        date_attestation = st.date_input("Date de l'attestation")

        submit_button = st.form_submit_button("Générer PDF")

    if submit_button:
        data = {
            'genre': genre,
            'type_stage': typeStage,
            'nom': nom,
            'prenom': prenom,
            'stage_intitule': stage_intitule,
            'date_debut': format_date_to_french(date_debut.strftime('%Y-%m-%d')),
            'date_fin': format_date_to_french(date_fin.strftime('%Y-%m-%d')),
            'service': service,
            'date_attestation': format_date_to_french(date_attestation.strftime('%Y-%m-%d')),
            'responsable_nom': responsable_nom,
            'responsable_titre': responsable_titre
        }

        # Generate PDF and save to a BytesIO object
        pdf_buffer = BytesIO()
        try:
            generate_pdf(data, output_stream=pdf_buffer, logo_path='C:/Users/Lenovo/app-starter-kit/myenv/logo.jpg')
            pdf_buffer.seek(0)  # Move the pointer to the beginning of the stream

            # Provide the PDF for download
            st.success("PDF généré avec succès!")
            st.download_button(
                label="Télécharger le PDF",
                data=pdf_buffer.getvalue(),  # Use getvalue() to get the binary data
                file_name="attestation_stage.pdf",
                mime="application/pdf"
            )
        except Exception as e:
            st.error(f"Erreur lors de la génération du PDF: {e}")

if __name__ == "__main__":
    main()
