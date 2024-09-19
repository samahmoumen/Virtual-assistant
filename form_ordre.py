import streamlit as st
from generate_ordre import app2
from io import BytesIO
from datetime import datetime


def main():
    
    st.title("Ordre de Mission")

    with st.form(key='order_mission_form'):
        col1, col2 = st.columns(2)
        
        with col1:
            lieu = st.text_input("Lieu de l'intervention")
            technicien = st.text_input("Nom du technicien")
            montant = st.text_input("Montant (en Dhs)")
        
        with col2:
            duree = st.text_input("Durée de l'intervention")
            demande_par = st.text_input("Demande par")

        submit_button = st.form_submit_button("Générer PDF")

    if submit_button:
        data = {
            'lieu': lieu,
            'technicien': technicien,
            'montant': montant,
            'duree': duree,
            'demande_par': demande_par
        }

        # Generate PDF and save to a BytesIO object
        pdf_buffer = BytesIO()
        try:
            app2(data, output_stream=pdf_buffer, logo_path='C:/Users/Lenovo/app-starter-kit/myenv/logo.jpg')
            pdf_buffer.seek(0)  # Move the pointer to the beginning of the stream

            # Provide the PDF for download
            st.success("PDF généré avec succès!")
            st.download_button(
                label="Télécharger le PDF",
                data=pdf_buffer.getvalue(),  # Use getvalue() to get the binary data
                file_name="ORDRE DE MISSION.pdf",
                mime="application/pdf"
            )
        except Exception as e:
            st.error(f"Erreur lors de la génération du PDF: {e}")

if __name__ == "__main__":
    main()
